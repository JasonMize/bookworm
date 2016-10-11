from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from bookcases.viewsets import BookcaseViewSet

router = DefaultRouter()
router.register(r'bookcases', BookcaseViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]