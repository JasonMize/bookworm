from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from bookcases.viewsets import BookcaseViewSet, BookshelfViewSet

router = DefaultRouter()
router.register(r'bookcases', BookcaseViewSet)
router.register(r'bookshelves', BookshelfViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]