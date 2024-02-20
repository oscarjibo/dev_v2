"""
URL configuration for osiris_Dev project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() ssfunction: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from osiris_dev.views import bienvenida, modulos, categoria_edad, plantilla1, plantilla_parametros, plantilla_cargador, plantilla_shortcut, plantillahija, plantillahija2
from aplicaciones.automatizacion.views import *
urlpatterns = [
    path("admin/", admin.site.urls),
    path('',home)


]
