from django.views.generic import DetailView

from BoogeyBookAPP import views
from django.urls import path
from django.views.generic.edit import CreateView
from BoogeyBookAPP.models import BookRead
from BoogeyBookAPP.forms import BookForm

app_name = "boogeybookapp"

urlpatterns = [
    path('boogeybookapp/', views.home),
    path('create/',
         CreateView.as_view(
             model=BookRead,
             template_name='form.html',
             form_class=BookForm),
         name='book_create'),
    path('<int:pk>',
         DetailView.as_view(
             model=BookRead,
             template_name='book_detail.html'),
         name='book_detail'),
    path('edit/', views.edit_score_view),
]
