from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Jugador, Equipo, Pais, Torneo, Partido
from .forms import JugadorForm, EquipoForm, TorneoForm, PartidoForm

def index(request):
    return render(request, 'futbol/index.html')

def listar_jugadores(request):
    jugadores = Jugador.objects.all()
    return render(request, 'futbol/listar_jugadores.html', {'jugadores': jugadores})

def crear_jugador(request):
    if request.method == 'POST':
        form = JugadorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_jugadores')
    else:
        form = JugadorForm()
    return render(request, 'futbol/formulario_jugador.html', {'form': form})

def editar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    form = JugadorForm(request.POST or None, request.FILES or None, instance=jugador)
    if form.is_valid():
        form.save()
        return redirect('listar_jugadores')
    return render(request, 'futbol/formulario_jugador.html', {'form': form})

def eliminar_jugador(request, id):
    jugador = get_object_or_404(Jugador, id=id)
    jugador.delete()
    return redirect('listar_jugadores')

def listar_equipos(request):
    equipos = Equipo.objects.all()
    return render(request, 'futbol/listar_equipos.html', {'equipos': equipos})

def crear_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listar_equipos')
    else:
        form = EquipoForm()
    return render(request, 'futbol/formulario_equipo.html', {'form': form})

def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    form = EquipoForm(request.POST or None, request.FILES or None, instance=equipo)
    if form.is_valid():
        form.save()
        return redirect('listar_equipos')
    return render(request, 'futbol/formulario_equipo.html', {'form': form})

def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)
    equipo.delete()
    return redirect('listar_equipos')

def crear_torneo(request):
    if request.method == 'POST':
        form = TorneoForm(request.POST)
        if form.is_valid():
            torneo = form.save(commit=False)
            torneo.save()
            form.save_m2m()
            return redirect('index')
    else:
        form = TorneoForm()
    return render(request, 'futbol/formulario_torneo.html', {'form': form})

def crear_partido(request):
    if request.method == 'POST':
        form = PartidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PartidoForm()
    return render(request, 'futbol/formulario_partido.html', {'form': form})