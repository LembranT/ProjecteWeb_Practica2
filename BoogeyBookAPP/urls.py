from BoogeyBookAPP import views
from django.urls import path
from django.views.generic.edit import CreateView

urlpatterns = [
    path('homeTemplate', views.home),
    path('search/', views.search),
]