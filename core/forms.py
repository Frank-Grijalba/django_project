from django import forms
from blog.models import Registrado

#formularios para ser añadido a una vista (views.py)

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        # Validaciones a formulario admin
        email_base, proveedor= email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Utiliza correo con .edu")
        return email

# class RegForm(forms.Form):
#     nombre = forms.CharField(max_length=100)
#     email = forms.EmailField()
class ContactForm(forms.Form):
    nombre = forms.CharField()
    email = forms.EmailField()
    mensaje = forms.CharField(widget=forms.Textarea)

