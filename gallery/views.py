from django.shortcuts import render
from .models import Art

# Create your views here.

def all_paper(request):
    return render(request, 'paper.html')


def all_canvas(request):
    return render(request, 'canvas.html')