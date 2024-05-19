from ninja_extra import (
    ModelConfig,
    ModelControllerBase,
    ModelPagination,
    ModelSchemaConfig,
    api_controller,
    paginate,
    route,
)
from ninja_extra.ordering import Ordering, ordering
from ninja_extra.pagination import PageNumberPaginationExtra, PaginatedResponseSchema
from ninja_extra.searching import Searching, searching

from wallets.models import Wallet
from wallets.schemas import WalletSchema
from wallets.services import WalletService


@api_controller("wallets", tags=["Wallet"])
class WalletModelController(ModelControllerBase):
    service = WalletService()
    model_config = ModelConfig(
        model=Wallet,
        allowed_routes=["create", "patch", "find_one"],
        response_schema=WalletSchema,
        pagination=ModelPagination(),
        schema_config=ModelSchemaConfig(
            exclude=set(),
            read_only_fields=["id", "created_at", "updated_at", "balance"],
        ),
    )

    @route.get("/", response=PaginatedResponseSchema[WalletSchema])
    @paginate(PageNumberPaginationExtra)
    @searching(Searching, search_fields=["label"])
    @ordering(Ordering, ordering_fields=["label", "created_at", "updated_at"])
    def list(self):
        return self.service.get_all()
