from django.shortcuts import render
from django.views.generic import View,TemplateView, ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Mikrotik
from .models import Categoria
from login_RB_app.mikrotik_commands import MikrotikComandos
from . import forms
from django.contrib.auth.hashers import make_password
from login_RB_app.forms import MikrotikForm
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(TemplateView):
    template_name = 'index.html'

class ListMikrotikView(LoginRequiredMixin,ListView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = Mikrotik
    template_name = "login_RB_app/mikrotik_lista.html"
    context_object_name = 'mikrotiks'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('mikrotik')
        if query:
            mikrotik_lista = Mikrotik.objects.filter( descricao__icontains=query)
        else:
            mikrotik_lista = Mikrotik.objects.all()
        return mikrotik_lista

class DetailMikrotikView(LoginRequiredMixin,DetailView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = Mikrotik
    template_name = "login_RB_app/mikrotik_estatus.html"

class CreateMikrotikView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = Mikrotik
    form_class = MikrotikForm
    success_message = "%(descricao)s foi cadastrado com sucesso"
    def get_success_url(self):
        return reverse('app:lista')

class UpdateMikrotikView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = Mikrotik
    form_class = MikrotikForm
    success_message = "%(descricao)s foi atualizado com sucesso"
    def get_success_url(self):
        return reverse('app:lista')

class DeleteMikrotikView(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    model = Mikrotik
    success_message = "removido com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteMikrotikView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('app:lista')

class ResutadoComandoView(LoginRequiredMixin,TemplateView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    template_name = "login_RB_app/resultado_comandos.html"
    def resultado_comandos(self):
        if self.request.session.get('lista_resultado_comandos', False):
            return self.request.session.get('lista_resultado_comandos')


class AdicionarUserComandoView(LoginRequiredMixin,FormView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    form_class = forms.UserCommand
    template_name = 'login_RB_app/user_command_form.html'
    success_url = reverse_lazy('app:resultado_comandos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de(os)'
        return context

    def form_valid(self, form):
        self.send_comando(form.cleaned_data)
        return super(AdicionarUserComandoView, self).form_valid(form)

    def send_comando(self, valid_data):
        mk = MikrotikComandos()
        mks = user_filter_comando(valid_data)
        self.request.session['lista_resultado_comandos'] = mk.add_logins(mks,valid_data)
        pass

class AtualizarUserComandoView(LoginRequiredMixin,FormView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    form_class = forms.UserCommand
    template_name = 'login_RB_app/user_command_form.html'
    success_url = reverse_lazy('app:resultado_comandos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de(os)'
        return context

    def form_valid(self, form):
        self.send_comando(form.cleaned_data)
        return super(AtualizarUserComandoView, self).form_valid(form)

    def send_comando(self, valid_data):
        mk = MikrotikComandos()
        mks = user_filter_comando(valid_data)
        self.request.session['lista_resultado_comandos'] = mk.update_user(mks,valid_data)
        pass

class RemoverUserComandoView(LoginRequiredMixin,FormView):
    login_url = '/'
    redirect_field_name = 'redirect_to'
    form_class = forms.RemoverUserCommand
    template_name = 'login_RB_app/user_command_form.html'
    success_url = reverse_lazy('app:resultado_comandos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar'
        return context

    def form_valid(self, form):

        self.send_comando(form.cleaned_data)
        return super(RemoverUserComandoView, self).form_valid(form)

    def send_comando(self, valid_data):
        mk = MikrotikComandos()
        mks = user_filter_comando(valid_data)       
        self.request.session['lista_resultado_comandos'] = mk.remover_users(mks,valid_data)
        pass

def user_filter_comando(data):
    print(data)
    if data['escopo'] == 'mikrotik':
        mks = Mikrotik.objects.filter(descricao=data['mikrotik'])
    elif data['escopo'] == 'categoria':
        mks = Mikrotik.objects.filter(categoria__descricao=data['categoria'])
    else:
        mks = Mikrotik.objects.all()
    return mks
