from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Evento, Participante


class EventoForm(forms.ModelForm):
    """
    Formulario para crear y editar eventos.
    Usa ModelForm para basarse en el modelo Evento.
    """
    class Meta:
        model = Evento
        fields = ['nombre', 'fecha', 'ubicacion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre del evento'
            }),
            'fecha': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ubicación (opcional)'
            }),
        }
        labels = {
            'nombre': 'Nombre del Evento',
            'fecha': 'Fecha del Evento',
            'ubicacion': 'Ubicación',
        }

    def clean_fecha(self):
        """
        Validación personalizada: la fecha debe ser futura
        """
        fecha = self.cleaned_data.get('fecha')
        if fecha and fecha < timezone.now().date():
            raise ValidationError('La fecha del evento debe ser futura.')
        return fecha

    def clean_nombre(self):
        """
        Validación personalizada: máximo 100 caracteres
        """
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) > 100:
            raise ValidationError('El nombre no puede superar los 100 caracteres.')
        return nombre


class ParticipanteForm(forms.ModelForm):
    """
    Formulario para agregar participantes a un evento.
    """
    class Meta:
        model = Participante
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nombre completo del participante'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.com'
            }),
        }
        labels = {
            'nombre': 'Nombre del Participante',
            'email': 'Correo Electrónico',
        }

    def clean_email(self):
        """
        Validación: email en formato correcto
        """
        email = self.cleaned_data.get('email')
        if not '@' in email:
            raise ValidationError('Ingrese un correo electrónico válido.')
        return email