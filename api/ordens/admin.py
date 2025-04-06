from django.contrib import admin
from .models import OrdemServico, ProdutoOrdem

class ProdutoOrdemInline(admin.TabularInline):
    model = ProdutoOrdem
    extra = 1

@admin.register(OrdemServico)
class OrdemServicoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'status', 'criado_em', 'valor_total')
    list_filter = ('status', 'criado_em')
    search_fields = ('cliente__nome', 'descricao')
    inlines = [ProdutoOrdemInline]
    filter_horizontal = ('servicos',)
