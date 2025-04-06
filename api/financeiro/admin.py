from django.contrib import admin

# Register your models here.



'''
#v1.1
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from usuarios.models import Usuario

class StarkTechAdminSite(AdminSite):
    site_header = "STARK TECH MG"
    site_title = "Painel Administrativo"
    index_title = "Bem-vindo ao Sistema de Gestão"

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_admin_css'] = 'usuarios/css/custom_admin.css'
        return context

admin_site = StarkTechAdminSite(name='starktech_admin')
admin_site.register(Usuario, UserAdmin)
admin_site.register(Group)

# Opcional: registrar seus apps aqui
'''