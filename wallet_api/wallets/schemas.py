from typing import Optional

from ninja import FilterSchema, ModelSchema

from wallets.models import Wallet


class WalletFilterSchema(FilterSchema):
    label: Optional[str] = None


class CreateOrUpdateWalletSchema(ModelSchema):
    class Meta:
        model = Wallet
        fields = [
            "label",
        ]


class WalletSchema(ModelSchema):
    class Meta:
        model = Wallet
        fields = [
            "id",
            "label",
            "balance",
            "created_at",
            "updated_at",
        ]
