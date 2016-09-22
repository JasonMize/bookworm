from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.db.models import Count

from .models import Bookcase, Bookshelf

def bookcase_list(request):
    bookcases = Bookcase.objects.annotate(shelf_count=Count('bookshelf')).all()

    context = {
        "bookcases": bookcases,
    }
    return render(request, "bookcases/bookcase_list.html", context)

def bookcase_detail(request, id):
    bookcase = get_object_or_404(Bookcase, pk=id)
    bookshelves = bookcase.bookshelf_set.annotate(book_count=Count('book')).all()

    context = {
        "bookcase": bookcase,
        "bookshelves": bookshelves,
    }

    return render(request, "bookcases/bookcase_detail.html", context)

def bookshelf_detail(request, id):
    query_set = Bookshelf.objects.annotate(book_count=Count('book'))
    bookshelf = get_object_or_404(query_set, pk=id)
    books = bookshelf.book_set.all()

    context = {
        "bookshelf": bookshelf,
        "books": books,
    }

    return render(request, "bookcases/bookshelf_detail.html", context)
