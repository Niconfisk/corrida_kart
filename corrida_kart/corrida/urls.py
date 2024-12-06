from django.urls import path
from .views import (
    pagina_inicial, PilotoListView, PilotoDetailView, PilotoCreateView, PilotoUpdateView, PilotoDeleteView,
    CorridaListView, CorridaDetailView, CorridaCreateView, CorridaUpdateView, CorridaDeleteView,
)

urlpatterns = [
    # Página inicial
    path('', pagina_inicial, name='pagina-inicial'),

    # URLs para Pilotos
    path('pilotos/', PilotoListView.as_view(), name='piloto-list'),
    path('pilotos/<int:pk>/', PilotoDetailView.as_view(), name='piloto-detalhes'),
    path('pilotos/adicionar/', PilotoCreateView.as_view(), name='piloto-adicionar'),
    path('pilotos/<int:pk>/editar/', PilotoUpdateView.as_view(), name='piloto-editar'),
    path('pilotos/<int:pk>/deletar/', PilotoDeleteView.as_view(), name='piloto-deletar'),

    # URLs para Corridas
    path('corridas/', CorridaListView.as_view(), name='corrida-list'),
    path('corridas/<int:pk>/', CorridaDetailView.as_view(), name='corrida-detalhes'),
    path('corridas/adicionar/', CorridaCreateView.as_view(), name='corrida-adicionar'),
    path('corridas/<int:pk>/editar/', CorridaUpdateView.as_view(), name='corrida-editar'),
    path('corridas/<int:pk>/deletar/', CorridaDeleteView.as_view(), name='corrida-deletar'),
]
