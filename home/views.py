from django.shortcuts import render

# Create your views here.

def home(request): 
    """A view that displays an index page"""
    return render(request, "home.html")


def about(request):
    """A view that displays the about page"""
    return render(request, "about.html")