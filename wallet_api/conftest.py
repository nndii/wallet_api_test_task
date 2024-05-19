import pytest
from ninja.testing import TestClient

from transactions.factories import TransactionFactory
from transactions.models import Transaction
from wallet_api.api import ninja_api
from wallets.factories import WalletFactory
from wallets.models import Wallet


@pytest.fixture(scope="session")
def f_api_client() -> TestClient:
    return TestClient(ninja_api)


@pytest.fixture
def f_wallet() -> Wallet:
    return WalletFactory()


@pytest.fixture
def f_transaction(f_wallet: Wallet) -> Transaction:
    return TransactionFactory(wallet=f_wallet)
