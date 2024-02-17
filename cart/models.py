from django.db import models

class ShoppingCart(models.Model):
    product = models.JSONField(blank=True, null=True)
    quantity = models.IntegerField(default=0)
    session_id = models.CharField(max_length=255)
