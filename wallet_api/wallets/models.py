from decimal import Decimal

from django.db import models


class Wallet(models.Model):
    label = models.CharField(max_length=255, null=False, unique=True)
    balance = models.DecimalField(
        max_digits=65,
        decimal_places=18,
        default=Decimal("0.00"),
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "wallets"
