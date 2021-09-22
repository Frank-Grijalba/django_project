from django.http import HttpResponse

#soporta todas las rutas que vamos a crear las

def functionHello(request, *args, **kwargs):
    return HttpResponse("Hello World!")
