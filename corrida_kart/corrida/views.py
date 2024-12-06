from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Piloto, Corrida

# Create your views here.

def pagina_inicial(request):
    return render(request, 'pagina_inicial.html')

# Views de Piloto
class PilotoListView(ListView):
    model = Piloto
    template_name = 'piloto/piloto_list.html'


class PilotoDetailView(DetailView):
    model = Piloto
    template_name = 'piloto/piloto_detail.html'


class PilotoCreateView(CreateView):
    model = Piloto
    fields = ['nome', 'idade', 'equipe']
    template_name = 'piloto/piloto_form.html'


class PilotoUpdateView(UpdateView):
    model = Piloto
    fields = ['nome', 'idade', 'equipe']
    template_name = 'piloto/piloto_form.html'


class PilotoDeleteView(DeleteView):
    model = Piloto
    template_name = 'piloto/piloto_confirm_delete.html'
    success_url = reverse_lazy('piloto-list')


# Views de Corrida
class CorridaListView(ListView):
    model = Corrida
    template_name = 'corrida/corrida_list.html'


class CorridaDetailView(DetailView):
    model = Corrida
    template_name = 'corrida/corrida_detail.html'


class CorridaCreateView(CreateView):
    model = Corrida
    fields = ['nome', 'data', 'pilotos']
    template_name = 'corrida/corrida_form.html'


class CorridaUpdateView(UpdateView):
    model = Corrida
    fields = ['nome', 'data', 'pilotos']
    template_name = 'corrida/corrida_form.html'


class CorridaDeleteView(DeleteView):
    model = Corrida
    template_name = 'corrida/corrida_confirm_delete.html'
    success_url = reverse_lazy('corrida-list')
