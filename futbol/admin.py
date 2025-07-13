from django.contrib import admin
from .models import Pais, Equipo, Torneo, EquipoTorneo, Jugador, Partido

admin.site.register(Pais)
admin.site.register(Equipo)
admin.site.register(Torneo)
admin.site.register(EquipoTorneo)
admin.site.register(Jugador)
admin.site.register(Partido)
