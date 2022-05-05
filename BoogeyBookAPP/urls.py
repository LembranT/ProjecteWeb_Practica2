from BoogeyBookAPP import views
from django.urls import path
from django.views.generic.edit import CreateView
from myrestaurants.forms import RestaurantForm
from myrestaurants.models import Restaurant

urlpatterns = [
    path('homeTemplate', views.home),
    path('search/', views.search),
# Register a restaurant, from: /myrestaurants/create
    path('restaurants/create',
        CreateView.as_view(
            model=Restaurant,
            template_name='myrestaurants/form.html',
            form_class=RestaurantForm),
        name='restaurant_create'),
]