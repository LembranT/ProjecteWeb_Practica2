from django.http import HttpResponse
from django.shortcuts import render, redirect
from BoogeyBookAPP.models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def singup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # guardat a auth_user
            login(request, user)
            return render(request, "homeTemplate.html")
        else:
            return render(request, "autTemplate.html", {"form": form})
    else:
        form = UserCreationForm
        return render(request, "autTemplate.html", {"form": form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "loginTemplate.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def home(request):
    return render(request, "homeTemplate.html")


@login_required(login_url='/login/')
def search_view(request):
    if request.GET["data"]:
        # message="Book searched: %r" %request.GET["data"]
        book = request.GET["data"]
        books = Book.objects.filter(name__exact=book)
        return render(request, "results.html", {"books": books, "query": book})
    else:
        message = "You just entered nothing."
    return HttpResponse(message)


@login_required(login_url='/login/')
def search_read(request):
    return render(request, "search_book.html")


@login_required(login_url='/login/')
def results_read(request):
    if request.GET["data"]:
        book_name = request.GET["data"]
        books = BookRead.objects.filter(name__icontains=book_name)
        return render(request, "results_read_book.html", {"books": books, "book_name": book_name})
    else:
        message = "You just entered nothing."

    return HttpResponse(message)


@login_required(login_url='/login/')
def delete_book(request):
    if request.GET["bookname"]:
        # message="Book searched: %r" %request.GET["data"]
        book = request.GET["bookname"]
        books = BookRead.objects.filter(name__exact=book)

        print(request)
        print(book)

        try:
            books.delete()
            print("Book deleted successfully!")
        except:
            print("Book doesn't exists")
        return render(request, "homeTemplate.html", {"books": books, "query": book})

    else:
        message = "Error deleting book."

    return HttpResponse(message)


@login_required(login_url='/login/')
def update_book(request):
    if request.GET["bookname"]:
        # message="Book searched: %r" %request.GET["data"]
        book = request.GET["bookname"]
        modified = request.GET["modifiedScore"]
        if modified.isnumeric():
            if int(modified) > 10:
                modified = 10
        else:
            modified = 0
        books = BookRead.objects.filter(name__exact=book)

        for b in books:
            b.score = modified
            b.save()

        return render(request, "homeTemplate.html", {"books": books, "query": book})

    else:
        message = "You just entered nothing."

    return HttpResponse(message)


@login_required(login_url='/login/')
def my_reviews(request):
    all_entries = BookRead.objects.all()
    return render(request, "booksearch.html", {"books": all_entries})

@login_required(login_url='/login/')
def search_book(request):
    if request.GET["bookname"]:
        book = request.GET["bookname"]
        searched = Book.objects.filter(name__icontains=book)
        return render(request, "booksearch.html", {"books": searched})