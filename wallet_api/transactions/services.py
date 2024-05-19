from typing import Any

import structlog
from django.db import transaction
from django.db.models import Model
from ninja_extra import ModelService

from exceptions import ServiceException
from transactions.models import Transaction
from transactions.schemas import CreateTransactionSchema
from wallets.services import WalletService

logger = structlog.get_logger(__name__)


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
        wallet = self._wallet_service.get_for_update(
            schema.wallet,
        )
        if wallet is None:
            logger.info("Wallet not found", wallet_id=schema.wallet)
            raise InvalidWallet("Wallet not found")

        if (wallet.balance + schema.amount) < 0:
            logger.info(
                "Insufficient funds",
                wallet_id=wallet.id,
                amount=schema.amount,
                balance=wallet.balance,
            )
            raise InsufficientFunds("Insufficient funds")

        transaction = super().create(schema, **kwargs)
        wallet.balance += transaction.amount
        wallet.save()

        logger.info(
            "Transaction created",
            txid=transaction.txid,
            wallet_id=wallet.id,
            amount=transaction.amount,
        )
        return transaction
