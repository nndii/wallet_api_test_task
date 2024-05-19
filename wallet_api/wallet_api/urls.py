from django.urls import path

from wallet_api.api import ninja_api

urlpatterns = [
    path("api/", ninja_api.urls),
]
