from django.db import models
from django.shortcuts import reverse
from django.utils import timezone

from .utils import generate_transaction_id_code


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

    def get_sales_id(self):
        sale_obj = self.sale_set.first()
        return sale_obj.id

    def __str__(self) -> str:

        return f"id: {self.id}, product: {self.product.name}, quantity: {self.quantity}"


class Sale(models.Model):
    """Responsavel pelas vendas"""

    transaction_id = models.CharField(max_length=12, blank=True)
    positions = models.ManyToManyField(Position)
    total_price = models.FloatField(blank=True, null=True)
    customer = models.ForeignKey("customers.Customer", on_delete=models.CASCADE)
    salesman = models.ForeignKey("profiles.Profile", on_delete=models.CASCADE)
    created = models.DateTimeField(blank=True)
    update = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse("sales:detail", kwargs={"pk": self.pk})

    def save(self, *args, **kwargs):
        if self.transaction_id == "":
            self.transaction_id = generate_transaction_id_code()
        if self.created is None:
            self.created = timezone.now()
        return super().save(*args, **kwargs)

    def get_positions(self):
        return self.positions.all()

    def __str__(self):
        return f"Sales of the amount of R{self.total_price}"


class CSV(models.Model):
    file_name = models.FileField(upload_to="csvs")
    activated = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:

        return super().__str__(self.file_name)
