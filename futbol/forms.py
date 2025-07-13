from django import forms
from .models import Jugador, Equipo, Pais, Torneo, Partido
from django_select2.forms import Select2MultipleWidget
from django.core.exceptions import ValidationError

TEXT_INPUT_CLASSES = 'mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm'
SELECT_CLASSES = 'mt-1 block w-full pl-3 pr-10 py-2 text-base border border-gray-300 focus:outline-none focus:ring-blue-500 focus:border-blue-500 sm:text-sm rounded-md'
FILE_INPUT_CLASSES = 'mt-1 block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'

class JugadorForm(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Nombre del jugador'
            }),
            'edad': forms.NumberInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Edad'
            }),
            'posicion': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'pais': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'equipo': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': FILE_INPUT_CLASSES,
            }),
        }

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Nombre del equipo'
            }),
            'pais': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'entrenador': forms.TextInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Nombre del entrenador'
            }),
            'escudo': forms.ClearableFileInput(attrs={
                'class': FILE_INPUT_CLASSES,
            }),
        }

class TorneoForm(forms.ModelForm):
    class Meta:
        model = Torneo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Nombre del torneo'
            }),
            'pais': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'fecha_inicio': forms.DateInput(attrs={
                'type': 'date',
                'class': TEXT_INPUT_CLASSES,
            }),
            'fecha_fin': forms.DateInput(attrs={
                'type': 'date',
                'class': TEXT_INPUT_CLASSES,
            }),
            'equipos': Select2MultipleWidget(attrs={'class': SELECT_CLASSES}), # Usamos Select2MultipleWidget
        }

    def clean_equipos(self):
        equipos = self.cleaned_data.get('equipos')
        if not equipos:
            raise ValidationError("Debes seleccionar al menos dos equipos.")
        if equipos.count() < 2:
            raise ValidationError("Debes seleccionar al menos dos equipos.")
        return equipos

class PartidoForm(forms.ModelForm):
    class Meta:
        model = Partido
        fields = '__all__'
        widgets = {
            'fecha': forms.DateInput(attrs={
                'type': 'date',
                'class': TEXT_INPUT_CLASSES,
            }),
            'equipo_local': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'equipo_visitante': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'torneo': forms.Select(attrs={
                'class': SELECT_CLASSES,
            }),
            'goles_local': forms.NumberInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Goles local'
            }),
            'goles_visitante': forms.NumberInput(attrs={
                'class': TEXT_INPUT_CLASSES,
                'placeholder': 'Goles visitante'
            }),
        }