from django.urls import path
from django.conf import settings

from backend.views.Auth import Auth
from backend.views.Registries import Registries

urlpatterns = [
    path("auth", Auth.as_view()),
    path("registries", Registries.as_view()),
    path("registries/<str:regsitry_id>", Registries.as_view()),
]