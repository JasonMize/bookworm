from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=500, blank=True)
    wikipedia_url = models.URLField(blank=True)
    cover = models.ImageField(upload_to="cover-photos/", blank=True, null=True)
    date_added = models.DateTimeField(
        help_text="The date the book was added to a shelf",
        default=timezone.now, null=True, blank=True)
    bookshelf = models.ForeignKey('bookcases.Bookshelf', null=True, blank=True)
    authors = models.ManyToManyField('Author')
    genres = models.ManyToManyField('Genre')

    def get_authors(self):
        author_names = [author.name for author in self.authors.all()]
        return ", ".join(author_names)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("books:book_detail", args=[self.pk])

    def update_authors(self, author_names):
        authors_for_book = []
        for author_name in author_names:
            author, created = Author.objects.get_or_create(name=author_name)
            authors_for_book.append(author)

        if len(authors_for_book) > 0:
            self.authors.clear()
            self.authors.add(*authors_for_book)



class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Genre(models.Model):
    FICTION = 'fiction'
    NON_FICTION = 'non-fiction'

    CATEGORY_CHOICES = (
        (FICTION, 'Fiction',),
        (NON_FICTION, 'Non-fiction'),
    )
    
    name = models.CharField(max_length=50, unique=True)
    category = models.CharField(max_length=50, 
        default=NON_FICTION, choices=CATEGORY_CHOICES)

    def __str__(self):
        return "{}, {}".format(self.name, self.category)
