from django.contrib import admin
from .models import Usuarios, Persona, Horario

# Registrar el modelo Usuarios en el panel de administración
admin.site.register(Usuarios)

admin.site.register(Persona)
admin.site.register(Horario)