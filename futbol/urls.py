# futbol/urls.py

from django.urls import path
from . import views # Importamos solo las vistas de plantilla HTML
# La siguiente línea 'from . import api_views' DEBE SER ELIMINADA
# o comentada, ya que estas vistas no se usan aquí.
# from . import api_views # <-- ELIMINAR/COMENTAR ESTA LÍNEA

urlpatterns = [
    path('', views.index, name='index'),

    # Jugadores (rutas para las vistas de plantillas HTML)
    path('jugadores/', views.listar_jugadores, name='listar_jugadores'),
    path('jugadores/crear/', views.crear_jugador, name='crear_jugador'),
    path('jugadores/editar/<int:id>/', views.editar_jugador, name='editar_jugador'),
    path('jugadores/eliminar/<int:id>/', views.eliminar_jugador, name='eliminar_jugador'),

    # Equipos (rutas para las vistas de plantillas HTML)
    path('equipos/', views.listar_equipos, name='listar_equipos'),
    path('equipos/crear/', views.crear_equipo, name='crear_equipo'),
    path('equipos/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipos/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),

    # Torneos (rutas para las vistas de plantillas HTML)
    path('torneos/nuevo/', views.crear_torneo, name='crear_torneo'),
    # path('torneos/', views.listar_torneos, name='listar_torneos'), # Si creas esta vista HTML
    # path('torneos/editar/<int:id>/', views.editar_torneo, name='editar_torneo'), # Si creas esta vista HTML

    # Partidos (rutas para las vistas de plantillas HTML)
    path('partidos/nuevo/', views.crear_partido, name='crear_partido'),
    # path('partidos/', views.listar_partidos, name='listar_partidos'), # Si creas esta vista HTML
    # path('partidos/editar/<int:id>/', views.editar_partido, name='editar_partido'), # Si creas esta vista HTML
]

# ¡IMPORTANTE! Las rutas API REST NO VAN AQUÍ.
# Se incluyen directamente desde registro_futbol/urls.py
# usando path('api/', include('futbol.api_urls')).