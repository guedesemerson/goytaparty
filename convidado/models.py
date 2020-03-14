from django.conf import settings
from django.db import models
from evento.models import Evento
class Convidado(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    identidade = models.CharField(max_length=9)
    confirmado = models.BooleanField()
    evento = models.ManyToManyField(Evento)

    def __str__(self):
        return self.nome +'-'+ self.identidade






