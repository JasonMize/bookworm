from rest_framework import serializers

from books.serializers import BookSerializer

from .models import Bookcase, Bookshelf


class BookshelfSerializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()
    book_set = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Bookshelf
        fields = ('id', 'shelf_label', 'bookcase', 'book_count', 'book_set', )

    def get_book_count(self, obj):
        return obj.book_set.count()

class BookcaseSerializer(serializers.ModelSerializer):
    bookshelf_set = BookshelfSerializer(many=True, read_only=True)
    bookshelf_count = serializers.SerializerMethodField()

    class Meta:
        model = Bookcase
        fields = ('id', 'name', 'description', 'bookshelf_count', 'bookshelf_set', )
        read_only_fields = ('bookshelf_set', )

    def get_bookshelf_count(self, obj):
        return obj.bookshelf_set.count()
