from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .forms import RegForm

#soporta todas las rutas que vamos a crear y que son llamadas en urls.py

# Llamado con función
def functionHello(request, *args, **kwargs):
    return HttpResponse("Desde functionHello: Hello World!")

# LLamada de una página web
def index(request):
    form = RegForm()
    context = {
        "the_form": form,
    }
    return render(request, "index.html", context)