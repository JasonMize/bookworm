from django import forms

from .models import Book
from core.forms import BootstrapFormMixin

class BookForm(BootstrapFormMixin, forms.ModelForm):

    class Meta:
        model = Book

        fields = (
            'title',
            'description',
            'wikipedia_url',
            'cover',
            'bookshelf',
            'authors',
            'genres',
        )

        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'genres': forms.CheckboxSelectMultiple(),
        }