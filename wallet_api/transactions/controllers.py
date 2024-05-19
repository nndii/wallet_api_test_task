from ninja_extra.searching import searching, Searching
from ninja_extra import (
    ModelConfig,
    ModelControllerBase,
    ModelSchemaConfig,
    api_controller,
    paginate,
    route,
)
from exceptions import ServiceExceptionSchema
from ninja_extra.ordering import Ordering, ordering
from ninja_extra.pagination import PageNumberPaginationExtra, PaginatedResponseSchema

from transactions.models import Transaction
from transactions.schemas import (
    CreateTransactionSchema,
    TransactionSchema,
)
from transactions.services import TransactionService


@api_controller("transactions", tags=["Transaction"])
class TransactionModelController(ModelControllerBase):
    service = TransactionService()
    model_config = ModelConfig(
        model=Transaction,
        allowed_routes=["find_one"],
        response_schema=TransactionSchema,
        schema_config=ModelSchemaConfig(
            exclude=set(),
            read_only_fields=["id", "txid", "created_at", "updated_at"],
        ),
    )

    @route.post(
        "/",
        summary="Create a new transaction",
        response={
            201: TransactionSchema,
            400: ServiceExceptionSchema,
        },
    )
    def create(self, data: CreateTransactionSchema):
        return 201, self.service.create(data)

    @route.get(
        "/",
        summary="List all transactions",
        response=PaginatedResponseSchema[TransactionSchema],
    )
    @paginate(PageNumberPaginationExtra)
    @searching(Searching, search_fields=["wallet__label", "=txid"])
    @ordering(Ordering, ordering_fields=["created_at", "updated_at"])
    def list(
        self,
    ):
        return self.service.get_all()
