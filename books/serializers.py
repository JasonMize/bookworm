from rest_framework import serializers

from .models import Book, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', )

class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    author_names = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'description',
            'wikipedia_url',
            'cover',
            'date_added',
            'bookshelf',
            'author_names',
            'genres',
            'authors',
        )

    def create(self, validated_data):
        authors_data = validated_data.pop('authors')
        book = Book.objects.create(**validated_data)
        
        authors_for_book = []
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(name=author_data["name"])
            authors_for_book.append(author)

        if len(authors_for_book) > 0:
            book.authors.add(*authors_for_book)

        return book

    def update(self, instance, validated_data):
        authors_data = validated_data.pop('authors')
        
        for key, value in validated_data.items():
            setattr(instance, key, value)


        authors_for_book = []
        for author_data in authors_data:
            author, created = Author.objects.get_or_create(name=author_data["name"])
            authors_for_book.append(author)

        if len(authors_for_book) > 0:
            instance.authors.clear()
            instance.authors.add(*authors_for_book)

        return instance


    def get_author_names(self, obj):
        return obj.get_authors()
