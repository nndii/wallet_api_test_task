from ninja import ModelSchema

from transactions.models import Transaction


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
