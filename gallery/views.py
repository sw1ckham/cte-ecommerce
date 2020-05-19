from django.shortcuts import render
from .models import Art

# Create your views here.

def all_paper(request):
    art = Art.objects.all().filter(catergorie='paper')
    return render(request, 'paper.html', {"art": art})


def all_canvas(request):
    art = Art.objects.all().filter(catergorie='canvas')
    return render(request, 'canvas.html', {"art": art})