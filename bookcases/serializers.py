from rest_framework import serializers

from .models import Bookcase, Bookshelf

class BookshelfSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()

    class Meta:
        model = Bookshelf
        fields = (
            'id',
            'shelf_label',
            'bookcase',
            'book_count',
        )

    def get_book_count(self, bookshelf):
        return bookshelf.book_set.count()

class BookcaseSerializer(serializers.ModelSerializer):
    bookshelf_set = BookshelfSerializer(many=True, read_only=True)

    class Meta:
        model = Bookcase
        fields = ('id', 'name', 'description', 'bookshelf_set',)
