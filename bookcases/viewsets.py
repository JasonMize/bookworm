from rest_framework import viewsets

from .models import Bookcase, Bookshelf
from .serializers import BookcaseSerializer, BookshelfSerializer

class BookcaseViewSet(viewsets.ModelViewSet):
    queryset = Bookcase.objects.all()
    serializer_class = BookcaseSerializer

class BookshelfViewSet(viewsets.ModelViewSet):
    queryset = Bookshelf.objects.all()
    serializer_class = BookshelfSerializer