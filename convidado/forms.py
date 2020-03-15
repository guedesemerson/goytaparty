from evento.models import Evento
from django import forms
from django.forms import ModelForm
from .models import Convidado

class DateInput(forms.DateInput):
    input_type = 'date'

class ConvidadoForm(ModelForm):
    class Meta:
        model= Convidado
        fields = '__all__'

        widgets = {'user': forms.HiddenInput(), 'nascimento':DateInput()}

    def __init__(self, user, *args, **kwargs):
        super(ConvidadoForm, self).__init__(*args, **kwargs)
        self.fields['evento'].queryset = Evento.objects.filter(user=user)
