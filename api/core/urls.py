"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from core.views import home
import os

urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),

    # Rotas da API
    path('api/usuarios/', include('usuarios.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/produtos/', include('produtos.urls')),
    path('api/servicos/', include('servicos.urls')),
    path('api/ordens/', include('ordens.urls')),
    path('api/pedidos/', include('pedidos.urls')),
]

# Servir arquivos estáticos no modo dev
urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'core/static'))

'''
#ORIGINAL
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('produtos.urls')),
]
'''




'''
#ORIGINAL
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
'''