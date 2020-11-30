from django.contrib import admin
from .models import Proprietario, Pet, Service, Consulta
# Register your models here.

admin.site.register(Proprietario)
admin.site.register(Pet)
admin.site.register(Service)
admin.site.register(Consulta)


