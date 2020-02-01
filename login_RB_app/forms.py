from django import forms
from login_RB_app.models import Mikrotik

class MikrotikForm(forms.ModelForm):
    class Meta():
        model = Mikrotik
        fields = '__all__'

        widgets = {
          'password' : forms.PasswordInput(attrs={'class':'textinputclass'}),
        }

class AddUserCommands(forms.Form):
    name = forms.CharField(max_length=264)
    password = forms.CharField(widget=forms.PasswordInput(attrs={'maxlength': '40'}))
    nivel = forms.ChoiceField(choices=(("read", "leitura"),("write", "escrita"),("full", "Leitura/escritas")))
    escopo = forms.ChoiceField(widget=forms.RadioSelect(attrs={ 'class':'form-check form-check-inline' }), choices=(("ip", "por Mikrotik"),("categoria", "por Categoria"),("todos", "todos")))
    ip = forms.CharField(required=False, widget=forms.TextInput(attrs={'maxlength': '15'}))

class removerUserCommands(forms.Form):
    name = forms.CharField(max_length=264)
    escopo = forms.ChoiceField(widget=forms.RadioSelect(attrs={ 'class':'form-check form-check-inline' }), choices=(("ip", "por Mikrotik"),("categoria", "por Categoria"),("todos", "todos")))
    ip = forms.CharField(required=False, widget=forms.TextInput(attrs={'maxlength': '15'}))
