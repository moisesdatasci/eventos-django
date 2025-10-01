from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=200, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

    def clean(self):
        # Validación: la fecha debe ser futura
        if self.fecha and self.fecha < timezone.now().date():
            raise ValidationError({'fecha': 'La fecha del evento debe ser futura.'})

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'


class Participante(models.Model):
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} - {self.evento.nombre}"

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Participante'
        verbose_name_plural = 'Participantes'