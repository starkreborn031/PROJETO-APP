from django.contrib import admin
from .models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'valor_base', 'ativo', 'criado_em')
    search_fields = ('nome',)
    list_filter = ('ativo',)
