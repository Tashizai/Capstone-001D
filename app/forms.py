# app/forms.py

from django import forms

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
