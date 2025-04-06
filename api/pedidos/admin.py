from django.contrib import admin
from .models import Pedido, ItemPedido

class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [ItemPedidoInline]
    list_display = ['id', 'cliente', 'status', 'criado_em']
    list_filter = ['status', 'criado_em']

admin.site.register(Pedido, PedidoAdmin)
