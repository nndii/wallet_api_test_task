from django.db.models import Model
from ninja_extra import ModelService

from wallets.models import Wallet


class WalletService(ModelService):
    def __init__(self, model: type[Model] = Wallet) -> None:
        super().__init__(model)

    def get_for_update(self, pk: int) -> Wallet | None:
        try:
            return Wallet.objects.select_for_update().get(pk=pk)
        except Wallet.DoesNotExist:
            return None
