"""ecommerse URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the-include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from ecommerse import settings

urlpatterns = [
    path('clientes/', include('modulos.clientes.urls')),
    path('mensualidad/', include('modulos.mensualidad.urls')),
    path('maquinaria/', include('modulos.maquinaria.urls')),
    path('instrumentos/', include('modulos.instrumentos.urls')),
    path('finanzas/', include('modulos.finanzas.urls')),
    path('', include('modulos.login.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)