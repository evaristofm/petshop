from django.contrib import admin
from .models import Pet, Service, Consulta



@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especie', 'raca')
    list_display_links = ('id', 'nome', 'especie')
    search_fields = ('id', 'nome', 'especie', 'raca',
                     'idade', 'peso', 'nasc', 'sexo', 'porte')
    list_per_page = 20

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')
    list_display_links = ('id' ,'nome', 'preco')

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    pass


