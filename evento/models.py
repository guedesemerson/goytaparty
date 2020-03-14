from django.conf import settings
from django.db import models

class Evento(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    nome_festa = models.CharField(max_length=150)
    data = models.DateField()
    local = models.CharField(max_length=150)
    endereco = models.CharField(max_length=200)
    def __str__(self):
        return self.nome_festa
