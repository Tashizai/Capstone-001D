from django.contrib import admin

# Register your models here.
# app/admin.py

from django.contrib import admin
from .models import Usuarios

# Registrar el modelo Usuarios en el panel de administración
admin.site.register(Usuarios)
