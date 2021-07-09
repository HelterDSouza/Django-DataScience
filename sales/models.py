from django.db import models
from django.utils import translation


# Create your models here.
class Position(models.Model):
    """Classe responsavel pelo valor * quantidade"""

    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.FloatField(blank=True)
    created = models.DateTimeField(blank=True)

    def save(self, *args, **kwargs):
        self.price = self.product.price * self.quantity
        return super().save(*args, **kwargs)

    def __str__(self) -> str:

        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"


class Sale(models.Model):
    """Responsavel pelas vendas"""

    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True)
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    salesman = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    update = models.DateTimeField(auto_now=true)

    def __str__(self):
        return f"Sales of the amount of ${self.total_price}"
