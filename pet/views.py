from django.shortcuts import render

from .models import Proprietario, Pet, Service, Consulta

# Create your views here.

def index(request):
    props = Proprietario.objects.all()
    pets = Pet.objects.all()
    consultas = Consulta.objects.all()


    context = {'props': props,
                'pets': pets,
                'consultas': consultas }
    return render(request, 'base/index.html', context)