from rest_framework import viewsets
from django.db.models import Q

from .models import Book, Author
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            self.queryset = self.queryset.filter(title__icontains = query)

        return self.queryset