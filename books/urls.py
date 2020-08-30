from django.urls import path
from .views import (
    HomePageView,
    BookDetailPageView,
    CreateBookPageView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('details/<int:pk>', BookDetailPageView.as_view(), name='details'),
    path('title/new', CreateBookPageView.as_view(), name='add_title'),
]
