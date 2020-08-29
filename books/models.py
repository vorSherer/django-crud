from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=64)
    by_user = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    authors = models.CharField(max_length=64)
    comments = models.TextField(max_length=200, default='Enter description or comments')

    def __str__(self):
        return self.title
    
