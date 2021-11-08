"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core import views as core_view
from blog import views as blog_view
from django.conf import settings
from django.conf.urls.static import static

# Para que todos los url aparezcan sin problema, deben estar entre admin e index (hablando de la importacion core)
# eso si, si no se ha invocado la etiqueta -> href="{% url 'nombre_etiqueta' %} en este caso en navbar.html 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', core_view.functionHello, name='hello'),
    path('contact/', core_view.contact, name='contact'),
    path('', core_view.index, name='index'),
    path('about/', blog_view.about, name='about'),
    path('accounts/', include('registration.backends.default.urls')),
    path('create-form/', core_view.create_book_normal, name='create'),
]
# sección para rutas estaticas

if settings.DEBUG: # si el debugg de settings es verdad...
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)