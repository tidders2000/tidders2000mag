
from django.shortcuts import render, redirect, reverse

from django.contrib import auth
import os

from django.views.generic import TemplateView, ListView

# Create your views here.
""" passes list of events in the DB to the index page """
def index(request):
    

    return render(request, "index.html")

def article(request):
     return render(request, "article.html")
    