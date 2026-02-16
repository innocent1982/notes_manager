from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import UserView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("token/verify/", TokenVerifyView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
    path("create/", UserView.as_view(), name="create-user"),
    path("get/<int:id>/", UserView.as_view()),
    path("get/", UserView.as_view()),
    path("update/", UserView.as_view()),
]
