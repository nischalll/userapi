from django.db.models import base
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import (
   UserRegistrationViewSet,
   UserIDViewSet
)

router = DefaultRouter()
router.register("registeruser", UserRegistrationViewSet, basename="user-detail")
router.register("userid", UserIDViewSet, basename="user-id")



urlpatterns = [
    path("", include(router.urls)),
]
