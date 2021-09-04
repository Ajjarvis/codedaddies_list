import requests

from django.shortcuts import render
from django.http import request

from bs4 import BeautifulSoup


def home(request):
    return render(request, template_name='base.html')
# Create your views here.


def new_search(request):
    search = request.POST.get('search')
    stuff_for_frontend = {
        'search': search,
    }
    print("==>", search)
    return render(request, 'my_app/new_search.html', stuff_for_frontend)
