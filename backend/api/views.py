from django.shortcuts import render

# Create your views here.

def index(request):
    render (request, "index.html")