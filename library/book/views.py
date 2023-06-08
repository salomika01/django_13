from django.shortcuts import get_object_or_404, render
from .models import Book


def book_info(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book/info.html', {'book': book})
