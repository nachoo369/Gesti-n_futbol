# futbol/api_views.py

from rest_framework import generics
from .models import Jugador, Equipo, Pais, Torneo, Partido
from .serializers import (
    JugadorSerializer,
    EquipoSerializer,
    PaisBasicSerializer, # Usamos el básico para la lista de países
    PaisDetailSerializer, # Usamos el detallado para el detalle de un país
    TorneoSerializer,
    PartidoSerializer
)

# Jugadores
class JugadorListAPIView(generics.ListAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

class JugadorDetailAPIView(generics.RetrieveAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer

# Equipos
class EquipoListAPIView(generics.ListAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

class EquipoDetailAPIView(generics.RetrieveAPIView):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer

# Torneos
class TorneoListAPIView(generics.ListAPIView):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer

# Partidos
class PartidoListAPIView(generics.ListAPIView):
    queryset = Partido.objects.all()
    serializer_class = PartidoSerializer

# Paises
class PaisListAPIView(generics.ListAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisBasicSerializer # Para la lista, solo necesitamos nombre e ID

class PaisDetailAPIView(generics.RetrieveAPIView):
    queryset = Pais.objects.all()
    serializer_class = PaisDetailSerializer # Para el detalle, queremos todas las relaciones