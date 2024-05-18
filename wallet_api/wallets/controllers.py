from ninja.constants import NOT_SET
from ninja_extra import (
    ControllerBase,
    api_controller,
    route,
)


@api_controller("wallets", permissions=[], auth=NOT_SET)
class WalletAPIController(ControllerBase):
    @route.get("/")
    def list_wallets(self) -> dict:
        return {}

    @route.post("/")
    def create_wallet(self) -> dict:
        return {}
