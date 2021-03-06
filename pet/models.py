from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



class Service(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.FloatField()
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome


class Pet(models.Model):
    nome = models.CharField(max_length=50)
    especie = models.CharField(max_length=30)
    raca = models.CharField(max_length=30)
    peso = models.FloatField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    nasc = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, null=True)
    porte = models.CharField(max_length=30, blank=True)
    obs = models.TextField(null=True, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    services = models.ManyToManyField(Service, null=True, blank=True)
    #consultas = models.ManyToManyField(Consultas)

    class Meta:
        ordering = ['nome']

    def get_absolute_url(self):
        return reverse('pet-detail', kwargs={'pk': self.pk})


    def __str__(self):
        return self.nome


class Consulta(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    service = models.ManyToManyField(Service)
    data = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pet} - {self.data}"


