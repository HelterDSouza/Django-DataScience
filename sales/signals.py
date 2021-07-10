from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Sale


@receiver(m2m_changed, sender=Sale.positions.through)
def calculate_total_price(sender, instance, action, **kwargs):
    if action == "post_add" or action == "post_remove":
        instance.total_price = sum([item.price for item in instance.get_positions()])
        instance.save()
