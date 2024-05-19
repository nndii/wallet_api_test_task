from django.db.models import Model
from ninja_extra import ModelService

from wallets.models import Wallet


class WalletService(ModelService):
    def __init__(self, model: type[Model] = Wallet) -> None:
        super().__init__(model)

    def get_by_id(self, pk: int) -> Wallet | None:
        try:
            return self.get_one(pk)
        except Wallet.DoesNotExist:
            return None
