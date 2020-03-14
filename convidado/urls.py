from .views import listaconvidados, updateconvidado, novoConvidado, convidadoDelete
from django.urls import path

urlpatterns = [
    path('list/', listaconvidados,name='convidados'),
    path('update/<id>', updateconvidado,name='convidadoUpdate'),
    path('delete/<id>', convidadoDelete,name='convidadoDelete'),
    path('new/', novoConvidado,name='novoConvidado'),
]
