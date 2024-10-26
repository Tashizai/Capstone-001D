from django.urls import path
from app import views
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', views.login_view, name='login'),  # Página de inicio de sesión
    path('home/', views.home_view, name='home'),  # Página principal para usuarios normales
    path('admin-home/', views.admin_home_view, name='admin_home'),  # Página del administrador
    path('logout/', views.logout_view, name='logout'),  # Cerrar sesión
    path('crear-usuario/', views.crear_usuario, name='crear_usuario'),
    path('ver_horario/<int:usuario_id>/', views.ver_horario_usuario, name='ver_horario'),
    path('ver_horario_cualquiera/<int:usuario_id>/', views.ver_horario_usuario_cualquiera, name='ver_horario_cualquiera'),
    path('agregar-horario/', views.agregar_horario, name='agregar_horario'),
    path('editar-horario/', views.editar_horario, name='editar_horario'),
    path('calendario/', views.calendario, name='calendario'),
    path('calendario_admin/', views.calendario, name='calendario_admin'),
    path('agregar-evento/', views.agregar_evento, name='agregar_evento'),
    path('eliminar-evento/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('editar-evento/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('calendario-admin/', views.calendario_admin, name='calendario_admin'),
    path('agregar-evento-admin/', views.agregar_evento_admin, name='agregar_evento'),
    path('eliminar-evento-admin/<int:evento_id>/', views.eliminar_evento_admin, name='eliminar_evento'),
    path('editar-evento-admin/<int:evento_id>/', views.editar_evento_admin, name='editar_evento'),
    path('anuncios/', views.lista_anuncios, name='lista_anuncios'),
    path('anuncios/crear/', views.crear_anuncio, name='crear_anuncio'),
    path('anuncios/eliminar/<int:anuncio_id>/', views.eliminar_anuncio, name='eliminar_anuncio'),

]
