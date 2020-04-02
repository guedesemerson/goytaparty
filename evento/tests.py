from django.contrib.auth.models import User
from django.test import TestCase
from evento.models import Evento

class EventoTestCase(TestCase):
    def setUp(self):
        userEmerson = User.objects.get(id=2)
        Evento.objects.create(user=userEmerson, nome_festa="festaTeste", data="24/03/2020", local="Rio das Ostras", endereco="Jardim Bela vista")


    def test_ValicaEvento(self):
        assert Evento.objects.all().count() == 1
