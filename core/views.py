from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .forms import RegForm
from blog.models import Registrado

#soporta todas las rutas que vamos a crear y que son llamadas en urls.py

# Llamado con función
def functionHello(request, *args, **kwargs):
    return HttpResponse("Desde functionHello: Hello World!")

# LLamada de una página web
def index(request):
    form = RegForm(request.POST or None) # si solo dejamos request.POST aparecerá el mensaje campos obligatorios, con None los oculta
    # print (dir(form)) para conocer los atributos de form
    
    if form.is_valid():
        form_data = form.cleaned_data
        correo = form_data.get("email")
        nombre = form_data.get("nombre")
        obj = Registrado.objects.create(email=correo, nombre=nombre)

    # contexto es como los id que serán utilizados por ejemplo en las paginas web
    context = {
        "the_form": form,
    }
    return render(request, "index.html", context)