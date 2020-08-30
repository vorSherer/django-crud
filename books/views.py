from django.shortcuts import render
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
)
from .models import Book


class HomePageView(ListView):
    template_name = 'home.html'
    model = Book
    paginate_by = 10


class BookDetailPageView(DetailView):
    template_name = 'book_detail.html'
    model = Book


class CreateBookPageView(CreateView):
    template_name = 'add_title.html'
    model = Book
    fields = '__all__'


