from typing import Optional

from ninja import Field, FilterSchema, ModelSchema

from transactions.models import Transaction


class TransactionFilterSchema(FilterSchema):
    wallet_id: Optional[int] = None
    wallet_label: Optional[str] = Field(None, q=["wallet__label__icontains"])
    txid: Optional[str] = Field(None, q=["txid__icontains"])


class CreateTransactionSchema(ModelSchema):
    class Meta:
        model = Transaction
        fields = [
            "amount",
            "wallet",
        ]


class TransactionSchema(ModelSchema):
    class Meta:
        model = Transaction
        fields = [
            "id",
            "txid",
            "amount",
            "wallet",
            "created_at",
            "updated_at",
        ]
