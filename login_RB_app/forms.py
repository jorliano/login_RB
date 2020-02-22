from django import forms
from login_RB_app.models import Mikrotik
from login_RB_app.models import Categoria
from django.core.validators import ip_address_validators
from django.core.exceptions import ValidationError

class MikrotikForm(forms.ModelForm):
    class Meta():
        model = Mikrotik
        fields = '__all__'

        widgets = {
          'senha' : forms.PasswordInput(render_value=True, attrs={'class':'textinputclass'}),
          'ip' : forms.TextInput(attrs={'class':'ip_address'}),
        }
        labels = {
            'descricao': ('Descrição'),
        }


class UserCommand(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=264)
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '40'}))
    nivel = forms.ChoiceField(choices=(("read", "leitura"),("write", "escrita"),("full", "Leitura/escrita")))
    escopo = forms.ChoiceField(widget=forms.RadioSelect(), choices=(("mikrotik", "por Mikrotik"),("categoria", "por Categoria"),("todos", "todos")))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),required=False, empty_label=None)
    mikrotik = forms.ModelChoiceField(queryset=Mikrotik.objects.all(),required=False, empty_label=None)
    # ip = forms.GenericIPAddressField(protocol='IPv4',required=False, widget=forms.TextInput(attrs={'maxlength': '15','class':'ip_address'}))

class RemoverUserCommand(forms.Form):
    username = forms.CharField(label='Nome de Usuário',max_length=264)
    escopo = forms.ChoiceField(widget=forms.RadioSelect(), choices=(("mikrotik", "por Mikrotik"),("categoria", "por Categoria"),("todos", "todos")))
    categoria = forms.ModelChoiceField(queryset=Categoria.objects.all(),required=False, empty_label=None)
    mikrotik = forms.ModelChoiceField(queryset=Mikrotik.objects.all(),required=False, empty_label=None)
    # ip = forms.GenericIPAddressField(protocol='IPv4',required=False, widget=forms.TextInput(attrs={'maxlength': '15','class':'ip_address'}))
