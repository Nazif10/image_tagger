from rest_framework import routers
from django.urls import include, path

from image_tagger import views

router = routers.DefaultRouter()
router.register(r"images", views.ImageViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("rest-auth/", include("rest_auth.urls")),
]
