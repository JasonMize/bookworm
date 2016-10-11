from rest_framework import serializers

from .models import Bookcase, Bookshelf

class BookshelfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookshelf
        fields = ('id', 'shelf_label', 'bookcase', )

class BookcaseSerializer(serializers.ModelSerializer):
    bookshelf_set = BookshelfSerializer(many=True)

    class Meta:
        model = Bookcase
        fields = ('id', 'name', 'description', 'bookshelf_set',)
        read_only_fields = ('bookshelf_set', )
