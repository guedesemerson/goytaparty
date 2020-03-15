from django.forms import ModelForm
from django import forms
from .models import Evento

class DateInput(forms.DateInput):
    input_type = 'date'

class EventoForm(ModelForm):
    class Meta:
        model= Evento
        fields = '__all__'
        widgets = {'user': forms.HiddenInput(), 'data':DateInput()}



