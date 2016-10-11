from rest_framework import viewsets

from .models import Bookcase
from .serializers import BookcaseSerializer

class BookcaseViewSet(viewsets.ModelViewSet):
    queryset = Bookcase.objects.all()
    serializer_class = BookcaseSerializer