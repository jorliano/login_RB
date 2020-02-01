from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from . import models
from login_RB_app.mikrotik_commands import MikrotikComandos
#from django.http import HttpResponse
from . import forms

from django.contrib.auth.hashers import make_password
from login_RB_app.forms import MikrotikForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'


class ListMikrotikView(ListView):
    context_object_name = 'mikrotiks'
    model = models.Mikrotik
    template_name = "login_RB_app/mikrotik_lista.html"

class DetailMikrotikView(DetailView):
    #context_object_name = 'mikrotik_detail'
    model = models.Mikrotik
    template_name = "login_RB_app/mikrotik_estatus.html"


class CreateMikrotikView(SuccessMessageMixin,CreateView):
    model = models.Mikrotik
    form_class = MikrotikForm
    success_message = "%(name)s foi cadastrado com sucesso"
    def get_success_url(self):
        return reverse('app:lista')


class UpdateMikrotikView(SuccessMessageMixin,UpdateView):
    model = models.Mikrotik
    form_class = MikrotikForm
    success_message = "%(name)s foi atualizado com sucesso"
    def get_success_url(self):
        return reverse('app:lista')

class DeleteMikrotikView(SuccessMessageMixin,DeleteView):
    model = models.Mikrotik
    success_message = "removido com sucesso"
    def get_success_url(self):
        return reverse('app:lista')

def add_user_command(request):
    if request.method == 'POST':

        form = forms.AddUserCommands(request.POST)
        if form.is_valid():
            mk = MikrotikComandos()
            data = request.POST
            if data['escopo'] == 'ip':
                mks = models.Mikrotik.objects.filter(ip=data['ip'])
            elif data['escopo'] == 'categoria':
                mks = models.Mikrotik.objects.filter(categoria__name=data['categoria'])
            else:
                mks = models.Mikrotik.objects.all()


            lista = mk.add_logins(mks,data)
            for list in lista:
                print(list)
                if list['tipo'] == 'success':
                  messages.success(request, '%s %s' % (list['name'],list['msg']))
                else:
                  messages.warning(request, '%s  %s' % (list['name'],list['msg']))
            return redirect('app:lista')


    # if a GET (or any other method) we'll create a blank form
    else:
        categorias = models.Categoria.objects.all()
        form = forms.AddUserCommands
        return render(request, 'login_RB_app/user_command_form.html', {'form': form, 'categorias': categorias, 'titulo':'Cadasto de'})
def update_user_command(request):
    if request.method == 'POST':

        form = forms.AddUserCommands(request.POST)
        if form.is_valid():
            mk = MikrotikComandos()
            data = request.POST
            if data['escopo'] == 'ip':
                mks = models.Mikrotik.objects.filter(ip=data['ip'])
            elif data['escopo'] == 'categoria':
                mks = models.Mikrotik.objects.filter(categoria__name=data['categoria'])
            else:
                mks = models.Mikrotik.objects.all()


            lista = mk.update_user(mks,data)
            for list in lista:
                print(list)
                messages.add_message(request, list['tipo'] , '%s %s' % (list['name'],list['msg']))

            return redirect('app:lista')


    # if a GET (or any other method) we'll create a blank form
    else:
        categorias = models.Categoria.objects.all()
        form = forms.AddUserCommands

        return render(request, 'login_RB_app/user_command_form.html', {'form': form, 'categorias': categorias, 'titulo':'Edição de'})

def remove_user_command(request):
    if request.method == 'POST':

        form = forms.removerUserCommands(request.POST)

        if form.is_valid():
            mk = MikrotikComandos()
            data = request.POST
            if data['escopo'] == 'ip':
                mks = models.Mikrotik.objects.filter(ip=data['ip'])
            elif data['escopo'] == 'categoria':
                mks = models.Mikrotik.objects.filter(categoria__name=data['categoria'])
            else:
                mks = models.Mikrotik.objects.all()

            lista = mk.remover_users(mks,data)
            for list in lista:
                print(list)
                messages.add_message(request, list['tipo'] , '%s %s' % (list['name'],list['msg']))

            return redirect('app:lista')


    # if a GET (or any other method) we'll create a blank form
    else:
        categorias = models.Categoria.objects.all()
        form = forms.removerUserCommands

        return render(request, 'login_RB_app/user_command_form.html', {'form': form, 'categorias': categorias, 'titulo':'Remover'})
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
