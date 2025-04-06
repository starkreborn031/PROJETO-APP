from django.contrib import admin
from .models import Cliente, Dispositivo, Defeito, Servico

admin.site.register(Cliente)
admin.site.register(Dispositivo)
admin.site.register(Defeito)
admin.site.register(Servico)
