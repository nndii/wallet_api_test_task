import uuid

from django.db import models

from wallets.models import Wallet


class Transaction(models.Model):
    txid = models.UUIDField(null=False, default=uuid.uuid4, unique=True)
    wallet = models.ForeignKey(
        Wallet,
        on_delete=models.PROTECT,
        related_name="transactions",
    )
    amount = models.DecimalField(max_digits=65, decimal_places=18, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "transactions"
