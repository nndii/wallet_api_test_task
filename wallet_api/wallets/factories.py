# factories.py
import factory
from wallets.models import Wallet


class WalletFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Wallet

    label = factory.Faker("word")
    balance = factory.Faker(
        "pydecimal",
        left_digits=5,
        right_digits=18,
        positive=True,
    )
