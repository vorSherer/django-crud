from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
)
from .models import Book


class HomePageView(TemplateView):
    template_name = 'home.html'


class BooksPageView(ListView):
    template_name = 'collection.html'
    model = Book