from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils.timezone import now
from datetime import time
from django.conf import settings
from django.contrib.auth import get_user_model

class UsuarioManager(BaseUserManager):
    def create_user(self, run, nombre, apellido, password=None, **extra_fields):
        if not run:
            raise ValueError("El RUT es obligatorio.")
        user = self.model(run=run, nombre=nombre, apellido=apellido, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, run, nombre, apellido, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(run, nombre, apellido, password, **extra_fields)

class Usuarios(AbstractBaseUser, PermissionsMixin):
    ROLES = [
        ('Directivo', 'Directivo'),
        ('Profesor', 'Profesor'),
        ('Asistente', 'Asistente'),
    ]

    id_usuario = models.AutoField(primary_key=True)
    run = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(unique=True, null=True, blank=True)
    password = models.CharField(max_length=128)
    rol = models.CharField(max_length=10, choices=ROLES, default='Profesor')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'run'
    REQUIRED_FIELDS = ['nombre', 'apellido']

    objects = UsuarioManager()

    def __str__(self):
        return f"{self.nombre} {self.apellido} ({self.run})"
    

class Curso(models.Model):
    nombre = models.CharField(max_length=100)  # Ejemplo: "4to Básico A"

    def __str__(self):
        return self.nombre

class HorarioBase(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    dia_semana = models.CharField(
        max_length=9,
        choices=[
            ('LUNES', 'Lunes'), ('MARTES', 'Martes'), ('MIERCOLES', 'Miércoles'),
            ('JUEVES', 'Jueves'), ('VIERNES', 'Viernes')
        ]
    )
    bloque = models.CharField(max_length=50)
    asignatura = models.CharField(max_length=100, default="Sin asignatura")

    def __str__(self):
        return f"{self.usuario} - {self.dia_semana} - {self.bloque} - {self.asignatura}"

class HorarioExcepcional(models.Model):
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)  
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    dia_semana = models.CharField(max_length=9)
    bloque = models.CharField(max_length=50)

    def __str__(self):
        return f"Excepción: {self.usuario.nombre} ({self.fecha_inicio} - {self.fecha_fin})"
    
class Evento(models.Model):
    TIPOS_EVENTO = [
        ('reunion', 'Reunión'),
        ('evaluacion', 'Evaluación'),
        ('actividad', 'Actividad'),
        ('otro', 'Otro')
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    fecha = models.DateField()
    tipo = models.CharField(max_length=50, choices=TIPOS_EVENTO, default='otro')
    creador = models.ForeignKey(Usuarios, on_delete=models.CASCADE, related_name='eventos')
    compartido_con = models.ManyToManyField(Usuarios, related_name='eventos_compartidos', blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.fecha}"
    
class Anuncio(models.Model):
    GRUPO_CHOICES = [
        ('Todos', 'Todos'),
        ('Directivos', 'Directivos'),
        ('Profesores', 'Profesores'),
        ('Asistentes', 'Asistentes'),
    ]
    
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField()
    autor = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    grupo_destinatario = models.CharField(max_length=20, choices=GRUPO_CHOICES)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
User = get_user_model()

class Carpeta(models.Model):
    nombre = models.CharField(max_length=255)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='archivos/')
    tamano = models.PositiveIntegerField()  # Campo para almacenar el tamaño del archivo
    fecha_subida = models.DateTimeField(auto_now_add=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    carpeta = models.ForeignKey(Carpeta, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre