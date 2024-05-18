from django.urls import path

from ninja_extra import NinjaExtraAPI

ninja_api = NinjaExtraAPI(
    title="Wallet API",
    description="Test assignment for the backend developer position",
    urls_namespace="store",
)
ninja_api.auto_discover_controllers()


urlpatterns = [
    path("api/", ninja_api.urls),
]
