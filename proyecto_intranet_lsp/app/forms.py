# app/forms.py

from django import forms
from .models import Usuarios

class LoginForm(forms.Form):
    run = forms.CharField(
        max_length=9,
        label='RUT',
        widget=forms.TextInput(attrs={'placeholder': 'RUT', 'required': True})
    )
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'required': True})
    )




class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = ['run', 'nombre', 'apellido', 'email', 'is_active', 'is_staff']
        widgets = {
            'password': forms.PasswordInput(),  # Para campos de contraseña
        }