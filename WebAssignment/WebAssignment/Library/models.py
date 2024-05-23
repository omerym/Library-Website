from ast import mod
from django.db import models

# Create your models here.
class Book(models.Model):
    bookId = models.CharField(max_length=100, primary_key=True)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=50)
    catogery = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)
    isBorrowed = models.BooleanField(default=False)