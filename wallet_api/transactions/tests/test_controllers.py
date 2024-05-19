import pytest
import uuid
from ninja.testing import TestClient
from decimal import Decimal

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


@pytest.mark.django_db
def test_create_transaction(
    f_api_client: TestClient,
    f_wallet: Wallet,
) -> None:
    url = "/transactions/"
    f_wallet.balance = Decimal("100.00")
    f_wallet.save()

    payload = {"amount": "-50.00", "wallet_id": f_wallet.id}
    response = f_api_client.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["amount"] == payload["amount"]
    assert response.json()["wallet"] == f_wallet.id


@pytest.mark.django_db
def test_create_transaction_invalid_wallet(f_api_client: TestClient) -> None:
    url = "/transactions/"
    payload = {
        "amount": "-50.00",
        "wallet_id": 999999,
    }
    response = f_api_client.post(url, json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Wallet not found"


@pytest.mark.django_db
def test_create_transaction_insufficient_funds(
    f_api_client: TestClient,
    f_wallet: Wallet,
) -> None:
    url = "/transactions/"
    f_wallet.balance = Decimal("10.00")
    f_wallet.save()
    payload = {"amount": "-50.001", "wallet_id": f_wallet.id}
    response = f_api_client.post(url, json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Insufficient funds"


@pytest.mark.django_db
def test_list_transactions(
    f_api_client: TestClient,
    f_transaction: Transaction,
) -> None:
    url = "/transactions/"
    response = f_api_client.get(url, format="json")
    assert response.status_code == 200
    assert len(response.json()["results"]) > 0
    assert response.json()["results"][0] == {
        "id": f_transaction.id,
        "wallet": f_transaction.wallet.id,
        "amount": str(f_transaction.amount),
        "txid": f_transaction.txid,
        "created_at": f_transaction.created_at.isoformat(),
        "updated_at": f_transaction.updated_at.isoformat(),
    }


@pytest.mark.django_db
def test_filter_transactions(
    f_api_client: TestClient,
    f_wallet: Wallet,
) -> None:
    uuid_1 = uuid.uuid4()
    uuid_2 = uuid.uuid4()
    transaction1 = TransactionFactory(wallet=f_wallet, txid=uuid_1)
    TransactionFactory(wallet=f_wallet, txid=uuid_2)

    url = f"/transactions/?search={uuid_1}"
    response = f_api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1
    assert response.json()["results"][0]["txid"] == str(transaction1.txid)
