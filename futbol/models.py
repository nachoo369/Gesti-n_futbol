from django.db import models

class Pais(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Países"

    def __str__(self):
        return self.nombre

class Equipo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    entrenador = models.CharField(max_length=100)
    escudo = models.ImageField(upload_to='escudos/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Equipos"

    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_fin = models.DateField(null=True, blank=True)
    equipos = models.ManyToManyField(Equipo, through='EquipoTorneo', related_name='torneos_participados')

    class Meta:
        verbose_name_plural = "Torneos"

    def __str__(self):
        return self.nombre

class EquipoTorneo(models.Model):
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Equipos en Torneos"
        unique_together = ('equipo', 'torneo')

    def __str__(self):
        return f"{self.equipo.nombre} en {self.torneo.nombre}"

class Jugador(models.Model):
    POSICION_CHOICES = [
        ('ARQ', 'Arquero'),
        ('DEF', 'Defensa'),
        ('MED', 'Mediocampista'),
        ('DEL', 'Delantero'),
        ('OTR', 'Otro'),
    ]

    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    posicion = models.CharField(
        max_length=3,
        choices=POSICION_CHOICES,
        default='MED',
    )
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE, blank=True, null=True)
    foto = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Jugadores"

    def __str__(self):
        return f"{self.nombre} {self.get_posicion_display()}"

class Partido(models.Model):
    fecha = models.DateField()
    equipo_local = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_local')
    equipo_visitante = models.ForeignKey(Equipo, on_delete=models.CASCADE, related_name='partidos_visitante')
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    goles_local = models.IntegerField(default=0)
    goles_visitante = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Partidos"

    def __str__(self):
        return f"{self.equipo_local.nombre} vs {self.equipo_visitante.nombre} ({self.fecha})"