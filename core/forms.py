from django import forms
from blog.models import Registrado

#formularios para ser añadido a una vista (views.py)

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]

class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()