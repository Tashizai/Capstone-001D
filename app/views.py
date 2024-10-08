from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm

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