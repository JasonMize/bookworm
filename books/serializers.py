from rest_framework import serializers

from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'wikipedia_url',
            'date_added',
            'bookshelf',
            'authors',
            'genres',
        )

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors')

        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        authors_for_book = []
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(name=author_data['name'])
            authors_for_book.append(author)

        instance.authors.clear()
        instance.authors.add(*authors_for_book)

        return instance
