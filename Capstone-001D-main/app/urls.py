from django.urls import path
from app import views
from . import views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.login_view, name='login'),  # Página de inicio de sesión
    path('home/', views.home, name='home'),  # Página principal para usuarios normales
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver_horario/<int:usuario_id>/', views.ver_horario_usuario, name='ver_horario'),
    path('agregar-horario/', views.agregar_horario, name='agregar_horario'),
    path('editar-horario/', views.editar_horario, name='editar_horario'),
    path('calendario/', views.calendario, name='calendario'),
    path('agregar-evento/', views.agregar_evento, name='agregar_evento'),
    path('eliminar-evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('editar-evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('anuncios/', views.lista_anuncios, name='lista_anuncios'),
    path('anuncios/crear/', views.crear_anuncio, name='crear_anuncio'),
    path('anuncios/eliminar/<int:anuncio_id>/', views.eliminar_anuncio, name='eliminar_anuncio'),
    path('archivos/', views.archivos_view, name='vista_archivos'),
    path('crear_carpeta/', views.crear_carpeta, name='crear_carpeta'),
    path('archivos/subir/', views.subir_archivo, name='subir_archivo'),
    path('archivos/subir/<int:carpeta_id>/', views.subir_archivo_a_carpeta, name='subir_archivo_a_carpeta'),
    path('archivos/carpeta/<int:carpeta_id>/', views.ver_carpeta, name='ver_carpeta'),
    path('archivos/subir/', views.subir_archivo, name='subir_archivo'),
    path('archivos/eliminar/<int:archivo_id>/', views.eliminar_archivo, name='eliminar_archivo'),
    path('compartir/<str:tipo>/<int:recurso_id>/', views.compartir_recurso, name='compartir_recurso'),
    path('crear_subcarpeta/<int:carpeta_id>/', views.crear_subcarpeta, name='crear_subcarpeta'),
    path('compartidos/', views.ver_compartidos, name='ver_compartidos'),
    path('reuniones/', views.ver_reuniones, name='ver_reuniones'),
    path('reuniones/crear/', views.crear_reunion, name='crear_reunion'),
    path('reunion/<int:reunion_id>/', views.ver_reunion, name='ver_reunion'),
    path('usuarios/crear/', views.crear_usuario, name='crear_usuario'),
    path('usuarios/listar/', views.listado_usuarios, name='listado_usuarios'),
    path('usuarios/perfil/<int:id_usuario>/', views.ver_perfil_usuario, name='ver_perfil_usuario'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
