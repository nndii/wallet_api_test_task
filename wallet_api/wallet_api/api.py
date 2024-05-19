from django.http import HttpRequest, HttpResponse
from ninja_extra import NinjaExtraAPI

from exceptions import ServiceException


ninja_api = NinjaExtraAPI(
    title="Wallet API",
    description="Test assignment for the backend developer position",
    urls_namespace="store",
)
ninja_api.auto_discover_controllers()


@ninja_api.exception_handler(ServiceException)
def service_exception_handler(
    request: HttpRequest,
    exc: ServiceException,
) -> HttpResponse:
    return ninja_api.create_response(
        request,
        {"detail": exc.message},
        status=exc.status_code,
    )
