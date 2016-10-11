from rest_framework import serializers

from .models import Bookcase

class BookcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookcase
        fields = ('id', 'name', 'description', 'bookshelf_set' ,)
        read_only_fields = ('bookshelf_set', )
        depth = 1