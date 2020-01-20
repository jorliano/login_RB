from django import forms
from login_RB_app.models import Mikrotik

class NewMikrotikForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = Mikrotik
        fields = '__all__'
