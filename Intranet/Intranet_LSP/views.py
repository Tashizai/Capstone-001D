from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .models import Persona, Horario
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import time

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            run = form.cleaned_data.get('run')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=run, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos')

    return render(request, 'app/login.html', {'form': form})

def home_view(request):
    return render(request, 'app/home.html')  # Renderiza la plantilla home.html

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigir a la página de inicio de sesión después de cerrar sesión



def ver_horario(request, persona_id):
    persona = get_object_or_404(Persona, pk=persona_id)
    
    # Aquí obtenemos los horarios dinámicamente desde la base de datos
    horarios = Horario.objects.filter(persona=persona)
    
    # Bloques horarios específicos para cada día
    lunes_primera_clase = horarios.filter(dia_semana='LUNES', hora_inicio='08:30').first()
    lunes_segunda_clase = horarios.filter(dia_semana='LUNES', hora_inicio='10:20').first()
    lunes_tercera_clase = horarios.filter(dia_semana='LUNES', hora_inicio='12:10').first()
    lunes_cuarta_clase = horarios.filter(dia_semana='LUNES', hora_inicio='14:25').first()

    martes_primera_clase = horarios.filter(dia_semana='MARTES', hora_inicio='08:30').first()
    martes_segunda_clase = horarios.filter(dia_semana='MARTES', hora_inicio='10:20').first()
    martes_tercera_clase = horarios.filter(dia_semana='MARTES', hora_inicio='12:10').first()
    martes_cuarta_clase = horarios.filter(dia_semana='MARTES', hora_inicio='14:25').first()
    
    miercoles_primera_clase = horarios.filter(dia_semana='MIERCOLES', hora_inicio='08:30').first()
    miercoles_segunda_clase = horarios.filter(dia_semana='MIERCOLES', hora_inicio='10:20').first()
    miercoles_tercera_clase = horarios.filter(dia_semana='MIERCOLES', hora_inicio='12:10').first()
    miercoles_cuarta_clase = horarios.filter(dia_semana='MIERCOLES', hora_inicio='14:25').first()

    jueves_primera_clase = horarios.filter(dia_semana='JUEVES', hora_inicio='08:30').first()
    jueves_segunda_clase = horarios.filter(dia_semana='JUEVES', hora_inicio='10:20').first()
    jueves_tercera_clase = horarios.filter(dia_semana='JUEVES', hora_inicio='12:10').first()
    jueves_cuarta_clase = horarios.filter(dia_semana='JUEVES', hora_inicio='14:25').first()
    

    context = {
        'persona': persona,
        'lunes_primera_clase': lunes_primera_clase,
        'lunes_segunda_clase': lunes_segunda_clase,
        'lunes_tercera_clase': lunes_tercera_clase,
        'lunes_cuarta_clase': lunes_cuarta_clase,
        'martes_primera_clase': martes_primera_clase,
        'martes_segunda_clase': martes_segunda_clase,
        'martes_tercera_clase': martes_tercera_clase,
        'martes_cuarta_clase': martes_cuarta_clase,
        'miercoles_primera_clase': miercoles_primera_clase,
        'miercoles_segunda_clase': miercoles_segunda_clase,
        'miercoles_tercera_clase': miercoles_tercera_clase,
        'miercoles_cuarta_clase': miercoles_cuarta_clase,
        'jueves_primera_clase' : jueves_primera_clase,
        'jueves_segunda_clase' : jueves_segunda_clase,
        'jueves_tercera_clase': jueves_tercera_clase, 
        'jueves_cuarta_clase' : jueves_cuarta_clase, 

    }

    return render(request, 'app/horario.html', context)


BLOQUES_HORARIOS = {
    '08:30-10:00': (time(8, 30), time(10, 0)),
    '10:20-11:50': (time(10, 20), time(11, 50)),
    '12:15-13:40': (time(12, 15), time(13, 40)),
    '14:25-15:55': (time(14, 25), time(15, 55))
}

def guardar_horario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        horario_data = data.get('horario', [])

        # Asegúrate de que el usuario tiene una relación con Persona
        try:
            persona = request.user.persona  # Relación con el modelo Persona
        except Persona.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'No se encontró la persona asociada al usuario.'}, status=400)

        # Procesar cada clase del horario
        for clase in horario_data:
            dia = clase['dia']
            bloque = clase['hora']
            asignatura = clase['asignatura']

            # Verificar si el bloque horario está predefinido
            if bloque in BLOQUES_HORARIOS:
                hora_inicio, hora_fin = BLOQUES_HORARIOS[bloque]

                # Crear o actualizar la entrada del horario para la persona
                horario, created = Horario.objects.get_or_create(
                    persona=persona,
                    dia_semana=dia,
                    hora_inicio=hora_inicio,
                    hora_fin=hora_fin
                )
                horario.asignatura = asignatura
                horario.save()

        return JsonResponse({'status': 'success', 'message': 'Horario guardado exitosamente.'})

    return JsonResponse({'status': 'error', 'message': 'Método no permitido.'}, status=405)