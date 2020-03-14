from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Convidado
from .forms import ConvidadoForm
@login_required()
def listaconvidados(request):
    form = ConvidadoForm(request.user)
    usuario = request.user
    convidados = Convidado.objects.filter(
        user=request.user
    )
    return render(request, 'convidado/listaconvidados.html',{'convidados':convidados, 'form':form, 'usuario':usuario})

@login_required()
def updateconvidado(request, id):
    print(request.POST)
    convidado = Convidado.objects.get(id=id)
    form = ConvidadoForm(request.user,request.POST or None, instance=convidado)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('convidados')
    else:
        return render(request, 'convidado/convidadoUpdate.html', {'convidado': convidado, 'form': form})
@login_required()
def novoConvidado(request):
    form = ConvidadoForm(request.user, request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        form.save()
    return redirect('convidados')

@login_required()
def convidadoDelete(request, id):
    convidado = Convidado.objects.get(id=id)
    convidado.delete()
    return redirect('convidados')



