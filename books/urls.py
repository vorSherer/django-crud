from django.urls import path
from .views import (
    HomePageView,
    BooksPageView,
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('booklist/', BooksPageView.as_view(), name='collection'),
]
