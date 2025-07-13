# futbol/api_urls.py

from django.urls import path
from .api_views import (
    JugadorListAPIView, JugadorDetailAPIView,
    EquipoListAPIView, EquipoDetailAPIView,
    TorneoListAPIView,
    PartidoListAPIView,
    PaisListAPIView, PaisDetailAPIView
)

urlpatterns = [
    # Jugadores
    path('jugadores/', JugadorListAPIView.as_view(), name='api_jugadores_list'),
    path('jugadores/<int:pk>/', JugadorDetailAPIView.as_view(), name='api_jugadores_detail'),

    # Equipos
    path('equipos/', EquipoListAPIView.as_view(), name='api_equipos_list'),
    path('equipos/<int:pk>/', EquipoDetailAPIView.as_view(), name='api_equipos_detail'),

    # Torneos
    path('torneos/', TorneoListAPIView.as_view(), name='api_torneos_list'),

    # Partidos
    path('partidos/', PartidoListAPIView.as_view(), name='api_partidos_list'),

    # Paises
    path('paises/', PaisListAPIView.as_view(), name='api_paises_list'),
    path('paises/<int:pk>/', PaisDetailAPIView.as_view(), name='api_paises_detail'),
]