from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Proprietario, Pet, Service, Consulta

# Create your views here.

class PetListView(ListView):
    model = Pet
    context_object_name = 'pets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['proprietarios'] = Proprietario.objects.all()
        context['consultas'] = Consulta.objects.all()
        return context

class PetDetailView(DetailView):
    model = Pet
    context_object_name = 'pet'

class PetCreateView(CreateView):
    model = Pet
    context_object_name = 'pet'
    fields = ['nome', 'especie', 'raca']

class PetUpdateView(UpdateView):
    model = Pet
    template_name_suffix = '_update_form'
    fields = ['nome', 'especie', 'raca']
    success_url = reverse_lazy('pet-list')

class PetDeleteView(DeleteView):
    model = Pet
    context_object_name = 'pet'
    success_url = reverse_lazy('pet-list')