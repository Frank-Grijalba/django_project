from django import forms

#formulario para ser añadido a una vista
class RegForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    email = forms.EmailField()