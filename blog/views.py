from django.shortcuts import render

# Create your views here.

#soporta todas las rutas que vamos a crear y que son llamadas en urls.py
# LLamada de una página web
def about(request):
    return render(request, "about.html", {})