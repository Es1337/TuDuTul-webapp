from django.http import HttpResponse
from django.shortcuts import render


def index(request, *args, **kwargs):
    return render(request, 'tudutul-webapp/index.html')
