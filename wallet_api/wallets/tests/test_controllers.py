import pytest
from ninja.testing import TestClient

from wallet_api.api import ninja_api
from wallets.factories import WalletFactory
from wallets.models import Wallet


@pytest.fixture(scope="session")
def f_api_client() -> TestClient:
    return TestClient(ninja_api)


@pytest.fixture
def f_wallet() -> Wallet:
    return WalletFactory()


@pytest.mark.django_db
def test_create_wallet(
    f_api_client: TestClient,
) -> None:
    assert Wallet.objects.count() == 0
    url = "/wallets/"

    payload = {"label": "test"}
    response = f_api_client.post(url, json=payload)
    assert response.status_code == 201
    assert response.json()["label"] == "test"
    assert response.json()["balance"] == "0.00"
    assert Wallet.objects.count() == 1


@pytest.mark.django_db
def test_filter_transactions(
    f_api_client: TestClient,
) -> None:
    wallet_1 = WalletFactory()
    WalletFactory()

    url = f"/wallets/?search={wallet_1.label}"
    response = f_api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()["results"]) == 1
    assert response.json()["results"][0] == {
        "id": wallet_1.id,
        "label": wallet_1.label,
        "balance": str(wallet_1.balance),
        "created_at": wallet_1.created_at.isoformat(),
        "updated_at": wallet_1.updated_at.isoformat(),
    }