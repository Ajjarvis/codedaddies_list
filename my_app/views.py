from django.shortcuts import render
from django.http import request


def home(request):
    return render(request, template_name='base.html')
# Create your views here.
