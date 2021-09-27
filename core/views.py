from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from .forms import RegForm, RegModelForm
from blog.models import Registrado

#soporta todas las rutas que vamos a crear y que son llamadas en urls.py

# Llamado con función
def functionHello(request, *args, **kwargs):
    return HttpResponse("Desde functionHello: Hello World!")

# LLamada de una página web
def index(request):
    titulo = "Formulario de registro"
    # if request.user.is_authenticated():
    #     titulo = "Bienvenido %s" %(request.user)
    form = RegModelForm(request.POST or None)
    # form = RegForm(request.POST or None) # si solo dejamos request.POST aparecerá el mensaje campos obligatorios, con None los oculta
    # print (dir(form)) para conocer los atributos de form
    context = {
        "titulo": titulo,
        "the_form": form,
    }
    if form.is_valid():
        instance = form.save(commit=False) # Al tener commit en false inpide registros nuevos en la bd, esto se hace para poder modificar
        # objetos antes de guardarlos
        # Por ejemplo, en nuestro formulario el nombre no es un campo obligatorio, por eso en la siguiente linea de código vamos a modificar
        # que el campo nombre almacene por defecto un nombre cualquiera

        if not instance.nombre:
            instance.nombre = "Default"
        instance.save() # Con esta linea ya podemos grabar en nuestra BD
        context = {
            "titulo": "Gracias %s!" %(instance.nombre),
        }

        print (instance.timestamp)
        # form_data = form.cleaned_data
        # correo = form_data.get("email")
        # nombre = form_data.get("nombre")
        # obj = Registrado.objects.create(email=correo, nombre=nombre)

    # contexto es como los id que serán utilizados por ejemplo en las paginas web

    return render(request, "index.html", context)