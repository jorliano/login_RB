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


class IndexView(TemplateView):
    template_name = 'index.html'

class ListMikrotikView(ListView):
    model = Mikrotik
    template_name = "login_RB_app/mikrotik_lista.html"
    context_object_name = 'mikrotiks'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('mikrotik')
        if query:
            mikrotik_lista = Mikrotik.objects.filter( name__icontains=query)
        else:
            mikrotik_lista = Mikrotik.objects.all()
        return mikrotik_lista

class DetailMikrotikView(DetailView):
    model = Mikrotik
    template_name = "login_RB_app/mikrotik_estatus.html"

class CreateMikrotikView(SuccessMessageMixin,CreateView):
    model = Mikrotik
    form_class = MikrotikForm
    success_message = "%(name)s foi cadastrado com sucesso"
    def get_success_url(self):
        return reverse('app:lista')

class UpdateMikrotikView(SuccessMessageMixin,UpdateView):
    model = Mikrotik
    form_class = MikrotikForm
    success_message = "%(name)s foi atualizado com sucesso"
    def get_success_url(self):
        return reverse('app:lista')

class DeleteMikrotikView(SuccessMessageMixin,DeleteView):
    model = Mikrotik
    success_message = "removido com sucesso"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeleteMikrotikView, self).delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('app:lista')

class ResutadoComandoView(TemplateView):
    template_name = "login_RB_app/resultado_comandos.html"
    def resultado_comandos(self):
        if self.request.session.get('lista_resultado_comandos', False):
            return self.request.session.get('lista_resultado_comandos')

# def add_user_command(request):
#     if request.method == 'POST':
#
#         form = forms.AddUserCommand(request.POST)
#         if form.is_valid():
#             mk = MikrotikComandos()
#             data = request.POST
#             mks = user_filter_comando(data)
#
#             request.session['lista_resultado_comandos'] = mk.add_logins(mks,data)
#             return redirect('app:resultado_comandos')
#         else:
#             categorias = Categoria.objects.all()
#             return render(request,'login_RB_app/user_command_form.html', {'form': form,'categorias': categorias,'titulo':'Cadastro de'})
#
#     else:
#         categorias = Categoria.objects.all()
#         form = forms.AddUserCommand
#         return render(request, 'login_RB_app/user_command_form.html', {'form': form, 'categorias': categorias, 'titulo':'Cadastro de'})
# def update_user_command(request):
#     if request.method == 'POST':
#
#         form = forms.AddUserCommand(request.POST)
#         if form.is_valid():
#             mk = MikrotikComandos()
#             data = request.POST
#             mks = user_filter_comando(data)
#             request.session['lista_resultado_comandos'] = mk.add_logins(mks,data)
#
#             return redirect('app:lista')
#     else:
#         categorias = Categoria.objects.all()
#         form = forms.AddUserCommand
#
#         return render(request, 'login_RB_app/user_command_form.html', {'form': form, 'categorias': categorias, 'titulo':'Edição de'})
class AddUserCommandtView(FormView):
    form_class = forms.UserCommand
    template_name = 'login_RB_app/user_command_form.html'
    success_url = reverse_lazy('app:resultado_comandos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Cadastro de(os)'
        return context

    def form_valid(self, form):
        self.send_comando(form.cleaned_data)
        return super(AdicionarUserCommandtView, self).form_valid(form)

    def send_comando(self, valid_data):
        mk = MikrotikComandos()
        mks = user_filter_comando(valid_data)
        self.request.session['lista_resultado_comandos'] = mk.add_logins(mks,valid_data)
        pass

class UpdateUserCommandtView(FormView):
    form_class = forms.UserCommand
    template_name = 'login_RB_app/user_command_form.html'
    success_url = reverse_lazy('app:resultado_comandos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Atualização de(os)'
        return context

    def form_valid(self, form):
        self.send_comando(form.cleaned_data)
        return super(AtualizarUserCommandtView, self).form_valid(form)

    def send_comando(self, valid_data):
        mk = MikrotikComandos()
        mks = user_filter_comando(valid_data)
        self.request.session['lista_resultado_comandos'] = mk.update_user(mks,valid_data)
        pass

class RemoveUserCommandtView(FormView):
    form_class = forms.RemoverUserCommand
    template_name = 'login_RB_app/user_command_form.html'
    success_url = reverse_lazy('app:resultado_comandos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Deletar'
        return context

    def form_valid(self, form):
        self.send_comando(form.cleaned_data)
        return super(RemoverUserCommandtView, self).form_valid(form)

    def send_comando(self, valid_data):
        mk = MikrotikComandos()
        mks = user_filter_comando(valid_data)
        self.request.session['lista_resultado_comandos'] = mk.remover_users(mks,valid_data)
        pass

def user_filter_comando(data):

    if data['escopo'] == 'ip':
        mks = Mikrotik.objects.filter(ip=data['ip'])
    elif data['escopo'] == 'categoria':
        mks = Mikrotik.objects.filter(categoria__name=data['categoria'])
    else:
        mks = Mikrotik.objects.all()
    return mks

 # mk.password = make_password(mk.password)
