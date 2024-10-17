from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Crear un administrador de usuarios personalizado
class UsuarioManager(BaseUserManager):
    def create_user(self, run, nombre, apellido, password=None, **extra_fields):
        if not run:
            raise ValueError("El RUT es obligatorio")
        user = self.model(run=run, nombre=nombre, apellido=apellido, **extra_fields)
        user.set_password(password)  # Establecer la contraseña con cifrado
        user.save(using=self._db)
        return user

    def create_superuser(self, run, nombre, apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(run, nombre, apellido, password, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    run = models.CharField(max_length=9, unique=True)  # RUT único
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    persona = models.OneToOneField('Persona', on_delete=models.SET_NULL, null=True, blank=True)  # Relación con Persona

    USERNAME_FIELD = 'run'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.run})"

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)  # Permitir nulo y valores en blanco
    rol = models.CharField(max_length=50)  # Puede ser 'Profesor', 'Asistente', etc.
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Horario(models.Model):
    DIAS_SEMANA = [
        ('LUNES', 'Lunes'),
        ('MARTES', 'Martes'),
        ('MIERCOLES', 'Miércoles'),
        ('JUEVES', 'Jueves'),
        ('VIERNES', 'Viernes'),
    ]
    
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=DIAS_SEMANA)
    bloque = models.CharField(max_length=50, default="08:30 - 10:00")  # Ejemplo: "08:30 - 10:00"
    asignatura = models.CharField(max_length=100, blank=True, null=True)
    clase = models.CharField(max_length=100, blank=True, null=True)  # Ejemplo: "4to Básico A"

    def __str__(self):
        return f"{self.asignatura} ({self.clase}) - {self.dia_semana} - {self.bloque}"