from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.models import Group
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import Usuarios, HorarioBase, HorarioExcepcional, Curso, Evento, Reunion
import json
from django.utils.timezone import now
import calendar
from datetime import date
from .models import Anuncio
from .forms import AnuncioForm
from .models import Carpeta, Archivo
from django.utils import timezone
from django.http import FileResponse, Http404
from django.http import HttpResponseForbidden
from django.utils.dateparse import parse_datetime

def login_view(request):
    if request.method == 'POST':
        run = request.POST.get('run')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, run=run, password=password)

        if user is not None:
            login(request, user)

            # Redirigir según el tipo de usuario
            if user.is_superuser or user.is_staff:  # Vista del admin
                return redirect('admin_home')
            else:  # Vista del usuario regular
                return redirect('home')
        else:
            return HttpResponse("Credenciales incorrectas. Inténtalo de nuevo.")

    return render(request, 'app/login.html')

@login_required
def home_view(request):
    # Obtener el usuario logueado
    usuario = get_object_or_404(Usuarios, id_usuario=request.user.id_usuario)

    # Días de la semana y bloques de horarios
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes']
    bloques = [
        "08:30 - 10:00 Primer bloque",
        "10:00 - 10:20 Recreo",
        "10:20 - 11:50 Segundo bloque",
        "11:50 - 12:10 Recreo",
        "12:10 - 13:40 Tercer bloque",
        "13:40 - 14:25 Almuerzo",
        "14:25 - 15:55 Último Bloque"
    ]

    # Crear una lista para almacenar los horarios de cada bloque y día
    horario_lista = []

    # Recorrer cada bloque y obtener la información para cada día
    for bloque in bloques:
        fila = [bloque]
        for dia in dias:
            asignacion = HorarioBase.objects.filter(usuario=usuario, dia_semana=dia.upper(), bloque=bloque).first()
            fila.append(asignacion)
        horario_lista.append(fila)

    context = {
        'usuario': usuario,
        'horario_lista': horario_lista,
        'dias': dias,
        'anuncios': [],  # Añade tus anuncios si tienes alguno
        'archivos': []   # Añade tus archivos si tienes alguno
    }

    return render(request, 'app/home.html', context)

@login_required
def admin_home_view(request):
    usuarios = Usuarios.objects.all()  # Obtener todos los usuarios

    context = {
        'usuarios': usuarios
    }
    return render(request, 'app/admin-home.html', context)

def logout_view(request):
    # Cerrar sesión y redirigir al login
    logout(request)
    return redirect('login')


@csrf_exempt
def crear_usuario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        run = request.POST.get('run')
        email = request.POST.get('email')
        rol = request.POST.get('rol')  # Capturando el rol correctamente
        password = request.POST.get('password')

        # Crear el usuario con los datos proporcionados
        nuevo_usuario = Usuarios.objects.create(
            nombre=nombre,
            apellido=apellido,
            run=run,
            email=email
        )
        nuevo_usuario.set_password(password)
        nuevo_usuario.save()

        # Asignar el grupo según el rol seleccionado
        try:
            grupo = Group.objects.get(name=rol)  # Verificar que el grupo exista
        except Group.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'El grupo no existe.'}, status=400)

        # Añadir el usuario al grupo
        nuevo_usuario.groups.add(grupo)

        return JsonResponse({'status': 'success', 'message': 'Usuario creado exitosamente.'})
    
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

BLOQUES_HORARIOS = {
    "08:30 - 10:00": "Primer Bloque",
    "10:00 - 10:20": "Recreo 1",
    "10:20 - 11:50": "Segundo Bloque",
    "11:50 - 12:10": "Recreo 2",
    "12:10 - 13:40": "Tercer Bloque",
    "13:40 - 14:25": "Almuerzo",
    "14:25 - 15:55": "Cuarto Bloque"
}

def ver_horario_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id_usuario=usuario_id)
    cursos = Curso.objects.all()

    # Días de la semana y bloques predeterminados
    dias = ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES']
    bloques = [
        "08:30 - 10:00 Primer bloque",
        "10:00 - 10:20 Recreo",
        "10:20 - 11:50 Segundo bloque",
        "11:50 - 12:10 Recreo",
        "12:10 - 13:40 Tercer bloque",
        "13:40 - 14:25 Almuerzo",
        "14:25 - 15:55 Ultimo Bloque"
    ]

    # Crear un diccionario con los horarios por (día, bloque)
    horarios = HorarioBase.objects.filter(usuario=usuario)
    horarios_dict = {(h.dia_semana, h.bloque): h for h in horarios}

    # Preparar los datos para el template
    horario_lista = []
    for bloque in bloques:
        fila = {
            'bloque': bloque,
            'datos': [horarios_dict.get((dia, bloque), None) for dia in dias]
        }
        horario_lista.append(fila)

    context = {
        'usuario': usuario,
        'cursos': cursos,
        'dias': dias,
        'bloques': bloques,  # Aseguramos que los bloques estén disponibles en el template
        'horario_lista': horario_lista,
    }

    return render(request, 'app/ver_horario.html', context)

@csrf_exempt
def agregar_horario(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id')
        curso_id = request.POST.get('curso')
        dia_semana = request.POST.get('dia_semana')
        bloque = request.POST.get('bloque')
        asignatura = request.POST.get('asignatura')

        try:
            usuario = Usuarios.objects.get(id_usuario=usuario_id)
            curso = Curso.objects.get(id=curso_id)

            HorarioBase.objects.create(
                usuario=usuario,
                curso=curso,
                dia_semana=dia_semana,
                bloque=bloque,
                asignatura=asignatura
            )
            return JsonResponse({'status': 'success', 'message': 'Horario añadido correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


def guardar_horario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        dia_semana = data.get('dia_semana')
        bloque = data.get('bloque')
        asignatura = data.get('asignatura')
        curso_id = data.get('curso')

        try:
            curso = Curso.objects.get(id=curso_id)
            usuario = Usuarios.objects.get(id=request.user.id)

            # Crear el horario
            HorarioBase.objects.create(
                usuario=usuario,
                curso=curso,
                dia_semana=dia_semana,
                bloque=bloque,
                asignatura=asignatura
            )
            return JsonResponse({'status': 'success', 'message': 'Horario añadido correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


@csrf_exempt
def editar_horario(request):
    if request.method == 'POST':
        horario_id = request.POST.get('horario_id')
        curso_id = request.POST.get('curso')
        dia_semana = request.POST.get('dia_semana')
        bloque = request.POST.get('bloque')
        asignatura = request.POST.get('asignatura')

        try:
            horario = HorarioBase.objects.get(id=horario_id)
            horario.curso_id = curso_id
            horario.dia_semana = dia_semana
            horario.bloque = bloque
            horario.asignatura = asignatura
            horario.save()

            return JsonResponse({'status': 'success', 'message': 'Horario editado correctamente.'})
        except HorarioBase.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Horario no encontrado.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@login_required
def calendario(request):
    today = date.today()

    # Filtrar eventos creados por el usuario o compartidos con el usuario autenticado
    if request.user.is_staff:
        # Si es admin, ve todos los eventos (propios y compartidos)
        eventos = Evento.objects.filter(creador=request.user) | Evento.objects.filter(compartido_con=request.user)
    else:
        # Si es usuario normal, solo ve sus eventos o eventos compartidos con él
        eventos = Evento.objects.filter(creador=request.user) | Evento.objects.filter(compartido_con=request.user)

    # Convertir el QuerySet a lista de diccionarios
    eventos_list = [
        {
            "id": evento.id,
            "titulo": evento.titulo,
            "descripcion": evento.descripcion,
            "fecha": evento.fecha.strftime("%Y-%m-%d"),
        }
        for evento in eventos
    ]

    # Obtener colegas para compartir eventos (excluyendo al usuario actual)
    colegas = Usuarios.objects.exclude(id_usuario=request.user.id_usuario)

    # Preparar año y mes actuales
    current_year = today.year
    current_month = today.month

    # Obtener número de días del mes actual
    import calendar
    _, dias_en_mes = calendar.monthrange(current_year, current_month)

    context = {
    'eventos': json.dumps(eventos_list),  # Convertimos los eventos a JSON
    'colegas': colegas,
    'today': today,
    'current_month': current_month,
    'current_year': current_year,
    'dias_del_mes': range(1, dias_en_mes + 1),
    'es_admin': request.user.is_staff  # Añadir esta bandera al contexto para identificar si es admin
    }

    return render(request, 'app/calendario.html', context)

@login_required
def agregar_evento(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        titulo = data.get('titulo')
        descripcion = data.get('descripcion')
        fecha = data.get('fecha')
        compartido_ids = data.get('compartido_con', [])

        try:
            evento = Evento.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha=fecha,
                creador=request.user
            )

            if compartido_ids:
                usuarios = Usuarios.objects.filter(id_usuario__in=compartido_ids)
                evento.compartido_con.set(usuarios)

            return JsonResponse({'status': 'success', 'message': 'Evento añadido correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


@login_required
def eliminar_evento(request, evento_id):
    if request.method == 'DELETE':
        try:
            evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
            evento.delete()
            return JsonResponse({'status': 'success', 'message': 'Evento eliminado correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


@login_required
def editar_evento(request, evento_id):
    if request.method == 'POST':
        try:
            evento = get_object_or_404(Evento, id=evento_id, creador=request.user)
            data = json.loads(request.body)

            evento.titulo = data.get('titulo', evento.titulo)
            evento.descripcion = data.get('descripcion', evento.descripcion)
            evento.fecha = data.get('fecha', evento.fecha)

            compartido_ids = data.get('compartido_con', [])
            if compartido_ids:
                usuarios = Usuarios.objects.filter(id_usuario__in=compartido_ids)
                evento.compartido_con.set(usuarios)

            evento.save()

            return JsonResponse({'status': 'success', 'message': 'Evento editado correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


def ver_horario_usuario_cualquiera(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id_usuario=usuario_id)
    cursos = Curso.objects.all()

    # Días de la semana y bloques predeterminados
    dias = ['LUNES', 'MARTES', 'MIERCOLES', 'JUEVES', 'VIERNES']
    bloques = [
        "08:30 - 10:00 Primer bloque",
        "10:00 - 10:20 Recreo",
        "10:20 - 11:50 Segundo bloque",
        "11:50 - 12:10 Recreo",
        "12:10 - 13:40 Tercer bloque",
        "13:40 - 14:25 Almuerzo",
        "14:25 - 15:55 Ultimo Bloque"
    ]

    # Crear un diccionario con los horarios por (día, bloque)
    horarios = HorarioBase.objects.filter(usuario=usuario)
    horarios_dict = {(h.dia_semana, h.bloque): h for h in horarios}

    # Preparar los datos para el template
    horario_lista = []
    for bloque in bloques:
        fila = {
            'bloque': bloque,
            'datos': [horarios_dict.get((dia, bloque), None) for dia in dias]
        }
        horario_lista.append(fila)

    context = {
        'usuario': usuario,
        'cursos': cursos,
        'dias': dias,
        'bloques': bloques,  # Aseguramos que los bloques estén disponibles en el template
        'horario_lista': horario_lista,
    }

    return render(request, 'app/horario_user.html', context)


def lista_anuncios(request):
    anuncios = Anuncio.objects.all().order_by('-fecha_creacion')
    ultimo_anuncio = anuncios.first()  # Obtener el último anuncio creado si existe
    anuncios_json = json.dumps(list(anuncios.values('id', 'titulo', 'descripcion', 'autor__nombre', 'grupo_destinatario')))
    return render(request, 'app/anuncios.html', {
        'anuncios': anuncios,
        'anuncios_json': anuncios_json,
        'ultimo_anuncio': ultimo_anuncio
    })


@csrf_exempt
def crear_anuncio(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        titulo = data.get('titulo')
        descripcion = data.get('descripcion')
        grupo_destinatario = data.get('grupo')
        
        # Crear el anuncio
        anuncio = Anuncio.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            grupo_destinatario=grupo_destinatario,
            autor=request.user
        )
        return JsonResponse({'message': 'Anuncio creado correctamente'}, status=201)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


@csrf_exempt
def eliminar_anuncio(request, anuncio_id):
    if request.method == 'DELETE':
        try:
            anuncio = get_object_or_404(Anuncio, id=anuncio_id)
            anuncio.delete()
            return JsonResponse({'status': 'success', 'message': 'Anuncio eliminado correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)



@login_required
def archivos_view(request):
    carpetas = Carpeta.objects.filter(usuario=request.user)
    archivos = Archivo.objects.filter(usuario=request.user, carpeta__isnull=True)  # Archivos sin carpeta
    usuarios = Usuarios.objects.exclude(id_usuario=request.user.id_usuario)  # Ajusta el campo `id` a `id_usuario`
    context = {
        'carpetas': carpetas,
        'archivos': archivos,
        'usuarios': usuarios,
    }
    return render(request, 'app/archivos.html', context)

@csrf_exempt
@login_required
def crear_carpeta(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')

            if not nombre:
                return JsonResponse({'status': 'error', 'message': 'Debe proporcionar un nombre para la carpeta.'}, status=400)

            # Crear la carpeta y asignar el usuario autenticado
            nueva_carpeta = Carpeta.objects.create(
                nombre=nombre,
                usuario=request.user  # Establecer el usuario autenticado como creador
            )

            return JsonResponse({'status': 'success', 'message': 'Carpeta creada correctamente.'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Datos mal formados.'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@csrf_exempt
@login_required
def subir_archivo(request):
    if request.method == 'POST':
        archivo = request.FILES.get('archivo')
        if archivo:
            try:
                nuevo_archivo = Archivo.objects.create(
                    nombre=archivo.name,
                    archivo=archivo,
                    tamano=round(archivo.size / 1024, 2),  # Tamaño en KB
                    usuario=request.user  # Registrar el usuario que sube el archivo
                )
                return JsonResponse({'status': 'success', 'message': 'Archivo subido exitosamente.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        return JsonResponse({'status': 'error', 'message': 'No se proporcionó archivo.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@csrf_exempt
@login_required
def subir_archivo_a_carpeta(request, carpeta_id):
    if request.method == 'POST':
        carpeta = get_object_or_404(Carpeta, id=carpeta_id)
        archivo = request.FILES.get('archivo')
        if archivo:
            try:
                nuevo_archivo = Archivo.objects.create(
                    nombre=archivo.name,
                    archivo=archivo,
                    tamano=round(archivo.size / 1024, 2),  # Tamaño en KB
                    carpeta=carpeta,
                    usuario=request.user  # Registrar el usuario que sube el archivo
                )
                return JsonResponse({'status': 'success', 'message': 'Archivo subido exitosamente.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
        return JsonResponse({'status': 'error', 'message': 'No se proporcionó archivo.'}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


@csrf_exempt
@login_required
def ver_carpeta(request, carpeta_id):
    carpeta = get_object_or_404(Carpeta, id=carpeta_id)

    # Verificar si el usuario tiene acceso a la carpeta (propietario o compartida)
    if carpeta.usuario != request.user and request.user not in carpeta.compartido_con.all():
        return HttpResponseForbidden("No tienes permisos para acceder a esta carpeta.")
    
    archivos = carpeta.archivos.all()  # Usamos el related_name definido en el modelo
    subcarpetas = carpeta.subcarpetas.all()  # Obtener todas las subcarpetas de la carpeta actual
    usuarios = Usuarios.objects.all()  # Obtener todos los usuarios para compartir

    if request.method == 'POST':
        # Manejar la subida de archivos dentro de una carpeta específica
        archivo = request.FILES.get('archivo')
        if archivo:
            # Solo el propietario puede subir archivos
            if carpeta.usuario == request.user:
                nuevo_archivo = Archivo.objects.create(
                    nombre=archivo.name,
                    archivo=archivo,
                    tamano=round(archivo.size / 1024, 2),  # Convertir a KB
                    carpeta=carpeta,
                    usuario=request.user  # Registrar el usuario que sube el archivo
                )
                return JsonResponse({'status': 'success', 'message': 'Archivo subido exitosamente.'})
            else:
                return JsonResponse({'status': 'error', 'message': 'No tienes permiso para subir archivos en esta carpeta.'}, status=403)

        return JsonResponse({'status': 'error', 'message': 'Error al subir el archivo.'}, status=400)

    context = {
        'carpeta': carpeta,
        'archivos': archivos,
        'subcarpetas': subcarpetas,
        'usuarios': usuarios  # Agregar usuarios al contexto
    }
    return render(request, 'app/ver_carpeta.html', context)


@login_required
def eliminar_archivo(request, archivo_id):
    if request.method == 'DELETE':
        try:
            archivo = Archivo.objects.get(id=archivo_id, usuario=request.user)
            archivo.delete()
            return JsonResponse({'status': 'success', 'message': 'Archivo eliminado correctamente.'})
        except Archivo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'El archivo no existe.'}, status=404)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@csrf_exempt
def compartir_recurso(request, tipo, recurso_id):
    if request.method == 'POST':
        try:
            # Parsear los datos enviados en la solicitud
            data = json.loads(request.body)
            usuarios_ids = data.get('usuarios', [])

            if not usuarios_ids:
                return JsonResponse({'status': 'error', 'message': 'No se han seleccionado usuarios para compartir.'}, status=400)

            usuarios = Usuarios.objects.filter(id_usuario__in=usuarios_ids)

            if tipo == 'archivo':
                recurso = get_object_or_404(Archivo, id=recurso_id)
                recurso.compartido_con.add(*usuarios)
            elif tipo == 'carpeta':
                recurso = get_object_or_404(Carpeta, id=recurso_id)
                recurso.compartido_con.add(*usuarios)
            else:
                return JsonResponse({'status': 'error', 'message': 'Tipo de recurso no válido.'}, status=400)

            return JsonResponse({'status': 'success', 'message': f'{tipo.capitalize()} compartido correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@csrf_exempt
@login_required
def crear_subcarpeta(request, carpeta_id):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            nombre = data.get('nombre')

            if not nombre:
                return JsonResponse({'status': 'error', 'message': 'Debe proporcionar un nombre para la subcarpeta.'}, status=400)

            # Obtener la carpeta padre donde se va a crear la subcarpeta
            carpeta_padre = get_object_or_404(Carpeta, id=carpeta_id)

            # Crear la subcarpeta y asignar el usuario autenticado
            nueva_carpeta = Carpeta.objects.create(
                nombre=nombre,
                usuario=request.user,  # Establecer el usuario autenticado como creador
                carpeta_padre=carpeta_padre  # Definir la carpeta padre
            )

            return JsonResponse({'status': 'success', 'message': 'Subcarpeta creada correctamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)


@csrf_exempt
@login_required
def ver_compartidos(request):
    usuario_actual = request.user

    # Obtener todas las carpetas compartidas con el usuario actual
    carpetas_compartidas = Carpeta.objects.filter(compartido_con=usuario_actual).select_related('usuario')

    # Obtener todos los archivos compartidos con el usuario actual
    archivos_compartidos = Archivo.objects.filter(compartido_con=usuario_actual).select_related('usuario')

    context = {
        'carpetas_compartidas': carpetas_compartidas,
        'archivos_compartidos': archivos_compartidos
    }

    return render(request, 'app/ver_compartidos.html', context)


@login_required
def ver_reuniones(request):
    usuario_actual = request.user
    ahora = timezone.now()

    # Los usuarios administradores pueden ver todas las reuniones
    if usuario_actual.is_staff or usuario_actual.is_superuser:
        reuniones_proximas = Reunion.objects.filter(fecha__gte=ahora).select_related('creador')
        reuniones_pasadas = Reunion.objects.filter(fecha__lt=ahora).select_related('creador')
        es_administrador = True
    else:
        reuniones_proximas = Reunion.objects.filter(fecha__gte=ahora, destinatarios=usuario_actual.rol).select_related('creador')
        reuniones_pasadas = Reunion.objects.filter(fecha__lt=ahora, destinatarios=usuario_actual.rol).select_related('creador')
        es_administrador = False

    context = {
        'reuniones_proximas': reuniones_proximas,
        'reuniones_pasadas': reuniones_pasadas,
        'es_administrador': es_administrador,
    }

    return render(request, 'app/reuniones.html', context)

@csrf_exempt
@login_required
def crear_reunion(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            titulo = data.get('titulo')
            descripcion = data.get('descripcion')
            fecha = data.get('fecha')
            destinatarios = data.get('destinatarios')
            creador = request.user  # Obtener el usuario actual como creador

            if not titulo or not fecha or not destinatarios or not descripcion:
                return JsonResponse({'status': 'error', 'message': 'Todos los campos son obligatorios.'}, status=400)

            nueva_reunion = Reunion.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                fecha=fecha,
                destinatarios=destinatarios,
                creador=creador
            )

            return JsonResponse({'status': 'success', 'message': 'Reunión creada exitosamente.'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)

@login_required
def ver_reunion(request, reunion_id):
    reunion = get_object_or_404(Reunion, id=reunion_id)

    context = {
        'reunion': reunion
    }

    return render(request, 'app/ver_reunion.html', context)