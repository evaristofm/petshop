from django.test import TestCase
from django.test import Client, TestCase

from .models import Pet, Proprietario, Service, Consulta


class ProprietarioTestCase(TestCase):

    def setUp(self):

        # Criando Proprietarios
        p1 = Proprietario.objects.create(name="Evaristo", phone='555555',
         email="evaisto@exemplo.com")
        p2 = Proprietario.objects.create(name="Aryanne", phone="5577999",
        email="arynne@exemplo.com")

        # Criando Pets

        Pet.objects.create(nome="Rash", especie="Cachorro", raca="Dashund", proprietario=p1)
        Pet.objects.create(nome="Max", especie="Cachorro", raca="Pitbull", proprietario=p2)
        Pet.objects.create(nome="Marley", especie="Cachorro", raca="Vira lata", proprietario=p1)

    def test_index(self):
        c = Client()
        response = c.get("/pets/")
        self.assertEqual(response.status_code, 200)
    
    
