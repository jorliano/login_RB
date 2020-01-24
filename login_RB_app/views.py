from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
from login_RB_app.mikrotik_commands import MikrotikComandos
#from django.http import HttpResponse
from . import forms

from django.contrib.auth.hashers import make_password
from login_RB_app.forms import MikrotikForm
from django.urls import reverse
from django.shortcuts import redirect


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

class CreateMikrotikView(CreateView):
    model = models.Mikrotik
    #template_name = "login_RB_app/mikrotik_cadastro.html"
    #fields = ('name','login','password','ip','categoria')
    form_class = MikrotikForm
    def get_success_url(self):
        return reverse('app:lista')


class UpdateMikrotikView(UpdateView):
    model = models.Mikrotik
    form_class = MikrotikForm
    def get_success_url(self):
        return reverse('app:lista')

class DeleteMikrotikView(DeleteView):
    model = models.Mikrotik
    def get_success_url(self):
        return reverse('app:lista')

def add_user_command(request):
    if request.method == 'POST':

        form = forms.AddUserCommands(request.POST)
        if form.is_valid():
            mk = MikrotikComandos()
            mks = models.Mikrotik.objects.all()
            data = request.POST
            mk.add_logins(mks,data)


            return redirect('app:lista')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = forms.AddUserCommands

    return render(request, 'login_RB_app/add_user_command.html', {'form': form})

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
