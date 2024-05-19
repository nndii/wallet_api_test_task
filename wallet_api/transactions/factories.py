import factory
from django.utils import timezone

from transactions.models import Transaction
from wallets.factories import WalletFactory


class TransactionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Transaction

    wallet = factory.SubFactory(WalletFactory)
    amount = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=18,
    )
    txid = factory.Faker("uuid4")
    created_at = factory.LazyFunction(timezone.now)
    updated_at = factory.LazyFunction(timezone.now)
