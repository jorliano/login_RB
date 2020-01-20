from django.shortcuts import render
#from django.http import HttpResponse
from login_RB_app.models import Mikrotik
#from . import forms
from login_RB_app.forms import NewMikrotikForm
from django.contrib.auth.hashers import make_password

def index(request):
    mikrotik_list = Mikrotik.objects.order_by('name')
    return render(request,'login_RB_app/index.html', {'mikrotiks': mikrotik_list})

def estatus(request):
    mikrotik = Mikrotik.objects.get(pk=request.id)
    return render(request,'login_RB_app/estatus.html', {'mikrotik': mikrotik})

def cadastrar(request):
    form = NewMikrotikForm()

    if request.method == 'POST':
        form = NewMikrotikForm(request.POST)
        if form.is_valid():
           #form.save(commit=True)
           mk = form.save()
           mk.password = make_password(mk.password)
           mk.save()
           return index(request)
        else:
           print('Erro ao salvar dados')

    return render(request,'login_RB_app/cadastro.html',{'form':form})

def editar(id,request):
    form = NewMikrotikForm()

    if request.method == 'UPDATE' and id != 0:
        form = NewMikrotikForm(request.UPDATE)
        if form.is_valid():
           #form.save(commit=True)
           mk = form.save()
           mk.password = make_password(mk.password)
           mk.save()
           return index(request)
        else:
           print('Erro ao editar dados')

    return render(request,'login_RB_app/edicao.html',{'form':form})
