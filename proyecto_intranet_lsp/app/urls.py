from django.urls import path
from .views import login_view, home_view, logout_view, user_list, user_create, user_edit, user_delete
from . import views

urlpatterns = [
    path('', login_view, name="login"),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),  # Nueva URL para cerrar sesión
    path('admin/usuarios/', user_list, name='user_list'),
    path('admin/usuarios/crear/', user_create, name='user_create'),
    path('admin/usuarios/editar/<int:user_id>/', user_edit, name='user_edit'),
    path('admin/usuarios/eliminar/<int:user_id>/', user_delete, name='user_delete'),
]
