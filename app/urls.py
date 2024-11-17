from django.urls import path
from .views import login_view, home_view, logout_view, admin_index, calendario_view, view_anuncios, archivos, compartidos, intranet_view, reuniones, videollamada

urlpatterns = [
    path('', login_view, name="login"),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),  # Nueva URL para cerrar sesión
    path('admin_index/', admin_index, name='admin_index'),
    path('calendario/', calendario_view, name='calendario'),
    path('anuncios/', view_anuncios, name='anuncios'),
    path('archivos/', archivos, name='archivos'),
    path('compartidos/', compartidos, name='compartidos'),
    path('intranet/', intranet_view, name='intranet'),
    path('reuniones/', reuniones, name='reuniones'),
    path('videollamada/', videollamada, name='videollamada'),
]

