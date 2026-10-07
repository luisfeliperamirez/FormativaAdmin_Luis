from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    credito_disponible = models.DecimalField(max_digits=10, decimal_places=2, default=0.00) 

    def __str__(self):
        return f"{self.nombre} (Crédito: ${self.credito_disponible})"


class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    numero_factura = models.CharField(max_length=50, unique=True)
    estado = models.CharField(max_length=20, default='Pendiente')
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.numero_factura} - Total: ${self.total}"

