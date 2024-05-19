from typing import Any

from django.db import transaction
from django.db.models import Model
from ninja_extra import ModelService

from exceptions import ServiceException
from transactions.models import Transaction
from transactions.schemas import CreateTransactionSchema
from wallets.services import WalletService


class InvalidWallet(ServiceException):
    pass


class InsufficientFunds(ServiceException):
    pass


class TransactionService(ModelService):
    def __init__(
        self,
        model: type[Model] = Transaction,
    ) -> None:
        super().__init__(model)
        self._wallet_service = WalletService()

    @transaction.atomic
    def create(
        self,
        schema: CreateTransactionSchema,
        **kwargs: Any,
    ) -> Any:
        wallet = self._wallet_service.get_by_id(
            schema.wallet,
        )
        if wallet is None:
            raise InvalidWallet("Wallet not found")

        Transaction.objects.filter(wallet=wallet).select_for_update().first()

        if (wallet.balance + schema.amount) < 0:
            raise InsufficientFunds("Insufficient funds")

        transaction = super().create(schema, **kwargs)
        wallet.balance += transaction.amount
        wallet.save()

        return transaction
