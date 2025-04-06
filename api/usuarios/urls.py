from django.urls import path

urlpatterns = [
    # rotas serão adicionadas aqui depois
]


'''
#v1.1
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Aqui você inclui as URLs de cada app
    path('api/usuarios/', include('usuarios.urls')),
    path('api/clientes/', include('clientes.urls')),
    path('api/produtos/', include('produtos.urls')),
    path('api/servicos/', include('servicos.urls')),
    path('api/ordens/', include('ordens.urls')),
    path('api/pedidos/', include('pedidos.urls')),
]
'''