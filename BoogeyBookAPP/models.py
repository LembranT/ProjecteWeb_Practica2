from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date


class Reader(models.Model):
    reader_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)


class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    country = models.CharField(max_length=20)
    books_published = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ISBN = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    release_date = models.DateField()


class BookRead(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    ISBN = models.CharField(max_length=20, default="")
    author = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE, null=True)
    genre = models.ForeignKey(Genre, related_name='genres', on_delete=models.CASCADE, null=True)
    score = models.IntegerField(default=0)
    review = models.TextField(max_length=1000, default='')
    release_date = models.DateField(default=date.today)

    def get_absolute_url(self):
        return reverse('boogeybookapp:book_detail', kwargs={'pk': self.pk})