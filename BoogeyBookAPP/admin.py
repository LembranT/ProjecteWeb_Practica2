from django.contrib import admin
from BoogeyBookAPP.models import Reader, Author, Genre, Book

admin.site.register(Reader)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)

# Register your models here.
