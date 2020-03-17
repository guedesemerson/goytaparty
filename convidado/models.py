from django.conf import settings
from django.db import models
from evento.models import Evento
class Convidado(models.Model):
    evento = models.ManyToManyField(Evento)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    nascimento = models.DateField()
    identidade = models.CharField(max_length=9,null=True, default=None, blank=True)
    confirmado = models.BooleanField()


    def __str__(self):
        return str(self.nome) +'-'+ str(self.identidade)






