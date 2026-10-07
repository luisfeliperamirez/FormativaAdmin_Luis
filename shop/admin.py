from django.contrib import admin
from .models import Cliente, Pedido

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono', 'mostrar_credito_clp')
    list_filter = ('credito_disponible',)
    search_fields = ('nombre', 'correo')

    @admin.display(description='Crédito Disponible')
    def mostrar_credito_clp(self, obj):
        return f"${int(obj.credito_disponible):,}".replace(",", ".")


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'cliente', 'fecha_pedido', 'estado', 'mostrar_total_clp')
    list_filter = ('estado', 'fecha_pedido')
    search_fields = ('numero_factura', 'cliente__nombre')

    @admin.display(description='Total')
    def mostrar_total_clp(self, obj):
        return f"${int(obj.total):,}".replace(",", ".")
