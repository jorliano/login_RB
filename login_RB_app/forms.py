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
    username = forms.CharField(max_length=264)
    password = forms.CharField(widget=forms.PasswordInput)
    nivel = forms.ChoiceField(choices=(("LEITURA", "leitura"),("TOTAL", "total")))
