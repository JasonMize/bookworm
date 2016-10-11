from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from bookcases.viewsets import BookcaseViewSet, BookshelfViewSet
from books.viewsets import BookViewSet

router = DefaultRouter()
router.register(r'bookcases', BookcaseViewSet)
router.register(r'bookshelves', BookshelfViewSet)
router.register(r'books', BookViewSet)


urlpatterns = [
    url(r'^', include(router.urls)),
]