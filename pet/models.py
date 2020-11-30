from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Proprietario(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_create = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.name

class Pet(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    peso = models.FloatField()
    idade = models.IntegerField()
    nasc = models.DateField()
    sexo = models.CharField(max_length=1)
    porte = models.CharField(max_length=30)
    obs = models.TextField(null=True, blank=True)

    prop = models.ManyToManyField(Proprietario)


    def __str__(self):
        return self.nome

class Service(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet} - {self.data}"




