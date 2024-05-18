from typing import Optional

from ninja import FilterSchema, Schema

from wallets.models import Wallet


class WalletFilterSchema(FilterSchema):
    label: Optional[str] = None


class CreateOrUpdateWalletSchema(Schema):
    class Meta:
        model = Wallet
        fields = [
            "label",
        ]


class WalletSchema(Schema):
    class Meta:
        model = Wallet
        fields = [
            "id",
            "label",
            "balance",
            "created_at",
            "updated_at",
        ]
