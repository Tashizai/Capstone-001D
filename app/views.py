from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import user_passes_test
from datetime import datetime

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            run = form.cleaned_data.get('run')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=run, password=password)

            if user is not None:
                login(request, user)  # Iniciar sesión
                if user.is_staff:  # Verificar si el usuario es superusuario
                    return redirect('admin_index')  # Redirigir a admin_index si es superusuario
                else:
                    return redirect('home')  # Redirigir a home si no es administrador
            else:
                messages.error(request, 'Credenciales inválidas. Por favor, inténtelo de nuevo.')  # Mensaje de error para credenciales incorrectas    

    return render(request, 'app/login.html', {'form': form})

def home_view(request):
    return render(request, 'app/home.html')  # Renderiza la plantilla home.html

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirigir a la página de inicio de sesión después de cerrar sesión

def admin_index(request):
    # Pasar el contexto con el nombre del usuario autenticado
    return render(request, 'app/admin_index.html')

def calendario_view(request):
    return render(request, 'app/calendario_view.html')

def view_anuncios(request):
    anuncios = [
        {'titulo': 'Reunión con personal administrativo', 'contenido': 'Un gusto en saludar, avisar que en la tarde de hoy...', 'autor': 'Pedro Jerez', 'destinatarios': 'Personal administrativos'},
        {'titulo': 'Reunión con personal administrativo', 'contenido': 'Un gusto en saludar, avisar que en la tarde de hoy...', 'autor': 'Pedro Jerez', 'destinatarios': 'Personal administrativos'},
        {'titulo': 'Reunión con personal administrativo', 'contenido': 'Un gusto en saludar, avisar que en la tarde de hoy...', 'autor': 'Pedro Jerez', 'destinatarios': 'Personal administrativos'},
        # Añadir más anuncios si es necesario
    ]

    # El anuncio seleccionado por defecto (primer anuncio)
    anuncio_seleccionado = anuncios[0] if anuncios else None

    return render(request, 'app/anuncios.html', {'anuncios': anuncios, 'anuncio_seleccionado': anuncio_seleccionado})


def archivos(request):
    archivos = [
        {"nombre": "CualquierArchivodeejemplo.docx", "fecha": "25 Sep 2024", "tamano": "15KB"},
        {"nombre": "CualquierArchivodeejemplo.docx", "fecha": "25 Sep 2024", "tamano": "15KB"},
        {"nombre": "CualquierArchivodeejemplo.docx", "fecha": "25 Sep 2024", "tamano": "15KB"},
    ]

    contexto = {
        "archivos": archivos,
    }
    
    return render(request, 'app/archivos.html', contexto)

def compartidos(request):
    return render(request, 'app/compartidos.html')

def intranet_view(request):
    return render(request, 'app/intranet.html')


def reuniones(request):
    # Datos de ejemplo para las reuniones
    sesiones = [
        {
            'titulo': 'Título reunión 1',
            'descripcion': 'Descripción de reunión 1',
            'fecha': datetime(2024, 11, 2)
        },
        {
            'titulo': 'Título reunión 2',
            'descripcion': 'Descripción de reunión 2',
            'fecha': datetime(2024, 11, 2)
        },
        {
            'titulo': 'Título reunión 3',
            'descripcion': 'Descripción de reunión 3',
            'fecha': datetime(2024, 11, 2)
        },
    ]
    
    return render(request, 'app/reuniones.html', {'sesiones': sesiones})

def videollamada(request):
    return render(request, 'app/videollamada.html')