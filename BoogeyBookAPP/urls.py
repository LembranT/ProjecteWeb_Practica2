from django.urls import path
from BoogeyBookAPP import views

urlpatterns = [
    path('homeTemplate', views.home),
    path('search/', views.search),
]