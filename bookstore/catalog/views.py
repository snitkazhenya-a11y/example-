from django.shortcuts import render
from django.db.models import Q, Count, Avg
from .models import Book, Category

def catalog_view(request):
    available_cheap_books = Book.objects.filter(price__lt=500, stock__gt=0)

    categories = Category.objects.annotate(total_books=Count('books'))

    context = {'available_cheap_books',
               'categories': categories
    }
    return render(request, 'index.html', context)
