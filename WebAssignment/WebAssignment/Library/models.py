from ast import mod
from asyncio.windows_events import NULL
from turtle import mode
from django.db import models
from django.contrib.auth.models import User
from django.db import models
# Create your models here.
class Book(models.Model):
    bookId = models.CharField(max_length=50, primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    category = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=255, null=True)
    borrowedBy = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, blank=True)