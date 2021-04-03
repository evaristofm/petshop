from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import ( 
    CreateView, UpdateView, DeleteView,
    FormView
)
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Pet, Service, Consulta


class CustomLoginView(LoginView):
    template_name = 'pet/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pet-list')

class RegisterPage(FormView):
    template_name = 'pet/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pet-list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pet-list')
        return super(RegisterPage, self).get(*args, **kwargs)

class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    context_object_name = 'pets'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['consultas'] = Consulta.objects.all()
        return context

class PetDetailView(LoginRequiredMixin, DetailView):
    model = Pet
    context_object_name = 'pet'

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    context_object_name = 'pet'
    fields = ['nome', 'especie', 'raca']
    success_url = reverse_lazy('pet-list')

class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    template_name_suffix = '_update_form'
    fields = ['nome', 'especie', 'raca']
    success_url = reverse_lazy('pet-list')

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    context_object_name = 'pet'
    success_url = reverse_lazy('pet-list')