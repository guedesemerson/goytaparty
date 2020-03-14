from django.forms import ModelForm
from django import forms

from .models import Evento

class EventoForm(ModelForm):
    class Meta:
        model= Evento
        fields = '__all__'
        widgets = {'user': forms.HiddenInput()}