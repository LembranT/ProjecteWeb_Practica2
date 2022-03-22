from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

#Frontend

#Definició pàgina principal
def home(request):
    
    return render(request, "homeTemplate.html")