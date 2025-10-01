from django.contrib import admin
from .models import Evento, Participante
# Register your models here.

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'fecha', 'ubicacion', 'fecha_creacion', 'contar_participantes']
    list_filter = ['fecha', 'fecha_creacion']
    search_fields = ['nombre', 'ubicacion']
    date_hierarchy = 'fecha'
    
    def contar_participantes(self, obj):
        return obj.participantes.count()
    contar_participantes.short_description = 'Participantes'


@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'evento', 'fecha_registro']
    list_filter = ['evento', 'fecha_registro']
    search_fields = ['nombre', 'email']
    date_hierarchy = 'fecha_registro'