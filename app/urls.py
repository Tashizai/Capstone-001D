from django.urls import path
from .views import login_view, home_view, logout_view, ver_horario
from . import views

urlpatterns = [
    path('', login_view, name="login"),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),  # Nueva URL para cerrar sesión
    path('horario/<int:persona_id>/', views.ver_horario, name='ver_horario'),
    path('guardar-horario/', views.guardar_horario, name='guardar_horario'),
]
