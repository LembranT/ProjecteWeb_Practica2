from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()


class BookRead(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('boogeybookapp:book_detail', kwargs={'pk': self.pk})
