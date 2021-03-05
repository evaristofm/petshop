from django.contrib import admin
from .models import Proprietario, Pet, Service, Consulta



class ProprietarioAdmin(admin.ModelAdmin):
    fields = ['name', 'phone', 'email']    
    list_display = ('id', 'name', 'email', 'phone', 'date_create')
    list_display_links = ('id', 'name', 'email')
    search_fields = ('id', 'name', 'email')
    list_per_page = 20

class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especie', 'raca')
    list_display_links = ('id', 'nome', 'especie')
    search_fields = ('id', 'nome', 'especie', 'raca',
                     'idade', 'peso', 'nasc', 'sexo', 'porte')
    list_per_page = 20

class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco')
    list_display_links = ('id' ,'nome', 'preco')


admin.site.register(Proprietario, ProprietarioAdmin)
admin.site.register(Pet, PetAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Consulta)


