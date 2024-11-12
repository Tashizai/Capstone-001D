from django.contrib import admin
from .models import Usuarios
from .models import Carpeta, Archivo

# Registrar el modelo Usuarios en el panel de administración
admin.site.register(Usuarios)
admin.site.register(Carpeta)
admin.site.register(Archivo)
