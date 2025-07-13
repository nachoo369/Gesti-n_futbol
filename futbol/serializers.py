# futbol/serializers.py

from rest_framework import serializers
from .models import Jugador, Equipo, Pais, Torneo, Partido

# Serializador básico para País, útil para anidar sin mucha información extra
class PaisBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre']

# Serializador básico para Equipo, útil para anidar sin mucha información extra (como en Partido)
class EquipoBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ['id', 'nombre', 'escudo'] # Incluir escudo si es relevante

# Serializador para Jugadores
class JugadorSerializer(serializers.ModelSerializer):
    pais_info = PaisBasicSerializer(source='pais', read_only=True) # Información anidada del país
    equipo_info = EquipoBasicSerializer(source='equipo', read_only=True, allow_null=True) # Información anidada del equipo

    class Meta:
        model = Jugador
        fields = [
            'id', 'nombre', 'edad', 'posicion', 'foto',
            'pais', 'pais_info', # ID y objeto anidado del país
            'equipo', 'equipo_info', # ID y objeto anidado del equipo
        ]

# Serializador para Equipos
class EquipoSerializer(serializers.ModelSerializer):
    pais_info = PaisBasicSerializer(source='pais', read_only=True)
    # Lista de jugadores de este equipo
    jugadores = JugadorSerializer(many=True, read_only=True, source='jugador_set') # Asume related_name por defecto 'jugador_set'

    class Meta:
        model = Equipo
        fields = [
            'id', 'nombre', 'entrenador', 'escudo',
            'pais', 'pais_info',
            'jugadores' # Lista anidada de jugadores
        ]

# Serializador para Partidos
class PartidoSerializer(serializers.ModelSerializer):
    equipo_local_info = EquipoBasicSerializer(source='equipo_local', read_only=True)
    equipo_visitante_info = EquipoBasicSerializer(source='equipo_visitante', read_only=True)
    torneo_nombre = serializers.CharField(source='torneo.nombre', read_only=True)

    class Meta:
        model = Partido
        fields = [
            'id', 'fecha', 'goles_local', 'goles_visitante',
            'equipo_local', 'equipo_local_info',
            'equipo_visitante', 'equipo_visitante_info',
            'torneo', 'torneo_nombre'
        ]

# Serializador para Torneos, con equipos participantes y cantidad de jugadores por equipo
class TorneoSerializer(serializers.ModelSerializer):
    pais_info = PaisBasicSerializer(source='pais', read_only=True)
    
    class Meta:
        model = Torneo
        fields = [
            'id', 'nombre', 'fecha_inicio', 'fecha_fin',
            'pais', 'pais_info',
            'equipos' # El campo ManyToMany para equipos
        ]

    # Sobreescribir to_representation para añadir "cantidad_jugadores" por cada equipo participante
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        
        equipos_participantes_data = []
        for equipo in instance.equipos.all():
            # Crear una representación más detallada del equipo para el torneo
            equipo_data = EquipoBasicSerializer(equipo).data
            # Añadir la cantidad de jugadores a la representación del equipo
            equipo_data['cantidad_jugadores'] = equipo.jugador_set.count() # Asume related_name por defecto 'jugador_set'
            equipos_participantes_data.append(equipo_data)
            
        # Reemplazar el campo 'equipos' original con la lista personalizada
        representation['equipos_participantes'] = equipos_participantes_data
        # Si no quieres que el ID de los equipos también aparezca en una lista 'equipos', puedes eliminarlo
        del representation['equipos'] 
        
        return representation

# Serializador para el detalle de un País, incluyendo sus equipos, jugadores y torneos
class PaisDetailSerializer(serializers.ModelSerializer):
    # Asume related_name por defecto 'equipo_set'
    equipos_del_pais = EquipoSerializer(many=True, read_only=True, source='equipo_set') 
    # Asume related_name por defecto 'jugador_set'
    jugadores_del_pais = JugadorSerializer(many=True, read_only=True, source='jugador_set')
    # Asume related_name por defecto 'torneo_set'
    torneos_del_pais = TorneoSerializer(many=True, read_only=True, source='torneo_set')

    class Meta:
        model = Pais
        fields = [
            'id', 'nombre',
            'equipos_del_pais',
            'jugadores_del_pais',
            'torneos_del_pais'
        ]