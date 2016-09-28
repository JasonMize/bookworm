from django import forms

from .models import Book
from core.forms import BootstrapFormMixin

class BookForm(BootstrapFormMixin, forms.ModelForm):

    author_names = forms.CharField(max_length=500)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['author_names'].initial = self.instance.get_authors()

    class Meta:
        model = Book

        fields = (
            'title',
            'description',
            'wikipedia_url',
            'cover',
            'author_names',
            'bookshelf',
            'genres',
        )

        widgets = {
            'description': forms.Textarea(attrs={'cols': 80, 'rows': 5}),
            'genres': forms.CheckboxSelectMultiple(),
        }

    def clean_author_names(self):
        authors_list = [name.strip() for name in self.cleaned_data['author_names'].split(',')]

        return authors_list
