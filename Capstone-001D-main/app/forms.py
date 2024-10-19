# app/forms.py

from django import forms

class LoginForm(forms.Form):
    run = forms.CharField(max_length=9, label="RUT", widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su RUT (sin puntos ni guión)',
        'class': 'input-class'
    }))
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese su contraseña',
        'class': 'input-class'
    }))