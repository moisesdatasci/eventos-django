from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('evento/crear/', views.crear_evento, name='crear_evento'),
    path('evento/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('evento/<int:evento_id>/participante/', views.agregar_participante, name='agregar_participante'),
]