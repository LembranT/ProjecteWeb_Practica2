from django.http import HttpResponse
from django.shortcuts import render, redirect
from BoogeyBookAPP.models import Book

# Create your views here.

# Autentication and register
from django.views.generic import View

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
            #login user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect("home")
    else:
        form = AuthenticationForm()

    return render(request, "loginTemplate.html", {"form": form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def home(request):
    return render(request, "homeTemplate.html")

@login_required(login_url='/login/')
def search_view(request):
    if request.GET["data"]:
        # message="Book searched: %r" %request.GET["data"]
        book = request.GET["data"]

        books = Book.objects.filter(name__icontains=book)

        return render(request, "results.html", {"books": books, "query": book})

    else:
        message = "You just entered nothing."

    return HttpResponse(message)
