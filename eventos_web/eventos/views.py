from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Evento, Participante
from .forms import EventoForm, ParticipanteForm

# Create your views here.
def inicio(request):
    """
    Página de inicio que muestra todos los eventos
    """
    eventos = Evento.objects.all()
    return render(request, 'eventos/inicio.html', {'eventos': eventos})


def crear_evento(request):
    """
    Vista para crear un nuevo evento.
    GET: Muestra el formulario vacío
    POST: Procesa y guarda el evento
    """
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            evento = form.save()
            messages.success(request, f'¡Evento "{evento.nombre}" creado exitosamente!')
            return redirect('detalle_evento', evento_id=evento.id)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = EventoForm()
    
    return render(request, 'eventos/crear_evento.html', {'form': form})


def detalle_evento(request, evento_id):
    """
    Muestra los detalles de un evento y sus participantes
    """
    evento = get_object_or_404(Evento, id=evento_id)
    participantes = evento.participantes.all()
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento,
        'participantes': participantes
    })


def agregar_participante(request, evento_id):
    """
    Vista para agregar un participante a un evento.
    GET: Muestra el formulario
    POST: Guarda el participante
    """
    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save(commit=False)
            participante.evento = evento
            participante.save()
            messages.success(request, f'¡Participante "{participante.nombre}" agregado exitosamente!')
            return redirect('detalle_evento', evento_id=evento.id)
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ParticipanteForm()
    
    return render(request, 'eventos/agregar_participante.html', {
        'form': form,
        'evento': evento
    })


def lista_eventos(request):
    """
    Lista completa de todos los eventos
    """
    eventos = Evento.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})