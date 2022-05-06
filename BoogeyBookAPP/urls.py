from BoogeyBookAPP import views
from django.urls import path
from django.views.generic.edit import CreateView
from BoogeyBookAPP.models import BookRead
from BoogeyBookAPP.forms import BookForm

app_name = "boogeybookapp"

urlpatterns = [
    path('home/', views.home),
    path('create',
         CreateView.as_view(
             model=BookRead,
             template_name='form.html',
             form_class=BookForm),
         name='book_create'),
]
