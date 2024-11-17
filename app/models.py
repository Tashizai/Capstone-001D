# app/models.py

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Crear un administrador de usuarios personalizado
class UsuarioManager(BaseUserManager):
    def create_user(self, run, nombre, apellido, password=None, **extra_fields):
        """
        Crear y guardar un usuario con el RUT y la contraseña especificados.
        """
        if not run:
            raise ValueError("El RUT es obligatorio")
        user = self.model(run=run, nombre=nombre, apellido=apellido, **extra_fields)
        user.set_password(password)  # Establecer la contraseña con cifrado
        user.save(using=self._db)
        return user

    def create_superuser(self, run, nombre, apellido, password=None, **extra_fields):
        """
        Crear y guardar un superusuario con el RUT, nombre, apellido y contraseña.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        return self.create_user(run, nombre, apellido, password, **extra_fields)

# Definir el modelo de Usuarios
class Usuarios(AbstractBaseUser, PermissionsMixin):
    id_usuario = models.AutoField(primary_key=True)
    run = models.CharField(max_length=9, unique=True)  # RUT único
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Definir el campo que se usará como nombre de usuario para el login
    USERNAME_FIELD = 'run'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.run})"
