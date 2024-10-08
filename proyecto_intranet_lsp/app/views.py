from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from .models import Usuarios
from .forms import UsuarioForm

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







# Vista para listar usuarios
def user_list(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'admin/user_list.html', {'usuarios': usuarios})

# Vista para crear usuario
def user_create(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente.')
            return redirect('user_list')
    else:
        form = UsuarioForm()
    return render(request, 'admin/user_form.html', {'form': form})

# Vista para editar usuario
def user_edit(request, user_id):
    usuario = get_object_or_404(Usuarios, pk=user_id)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario actualizado correctamente.')
            return redirect('user_list')
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'admin/user_form.html', {'form': form, 'usuario': usuario})

# Vista para eliminar usuario
def user_delete(request, user_id):
    usuario = get_object_or_404(Usuarios, pk=user_id)
    if request.method == 'POST':
        usuario.delete()
        messages.success(request, 'Usuario eliminado correctamente.')
        return redirect('user_list')
    return render(request, 'admin/user_confirm_delete.html', {'usuario': usuario})
