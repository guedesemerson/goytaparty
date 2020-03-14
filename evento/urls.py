from .views import (listaEvento,
                    updateEvento,
                    novoEvento,
                    eventoDelete,
                    convidadoEvento)
from django.urls import path


urlpatterns = [
    path('list/', listaEvento, name='eventos'),
    path('update/<id>', updateEvento, name='updateEvento'),
    path('delete/<id>', eventoDelete, name='deleteEvento'),
    path('new/', novoEvento, name='newEvento'),
    path('convidadoEvento/<id>',convidadoEvento, name='convidadoEvento')
]
