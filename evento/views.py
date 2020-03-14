from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Evento
from .forms import EventoForm
from convidado.models import Convidado
@login_required()
def listaEvento(request):
    form = EventoForm()
    eventos = Evento.objects.filter(
        user=request.user
    )
    return render(request, 'evento/listaevento.html',{'eventos':eventos, 'form':form})
@login_required()
def updateEvento(request, id):
    evento = Evento.objects.get(id=id)
    form = EventoForm(request.POST or None, instance=evento)

    if request.method == 'POST':
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('eventos')
    else:
        return render(request, 'evento/updateEvento.html', {'evento': evento, 'form': form})
@login_required()
def novoEvento(request):
    form = EventoForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
    return redirect('eventos')

@login_required()
def eventoDelete(request, id):
    evento = Evento.objects.get(id=id)
    evento.delete()
    return redirect('eventos')

@login_required()
def convidadoEvento(request, id):
    convidado = Convidado.objects.filter(
        evento = id, user=request.user
    )
    return render(request, 'evento/listaconvidadoevento.html', {'convidados': convidado})