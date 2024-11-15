from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import OrderItem, Bill

@receiver(post_save, sender=OrderItem)
def update_bill_total_on_save(sender, instance, **kwargs):
    """
    Updates the total amount of the associated Bill whenever an OrderItem is created or updated.
    """
    if instance.bill:
        instance.bill.update_total_amount()

@receiver(post_delete, sender=OrderItem)
def update_bill_total_on_delete(sender, instance, **kwargs):
    """
    Updates the total amount of the associated Bill whenever an OrderItem is deleted.
    """
    if instance.bill:
        instance.bill.update_total_amount()
