from django.shortcuts import render
from .models import Product

# Create your views here.

def all_products(request):
    """ A view to render all products """
    products = Product.objects.all()
    return render(request, "products.html", {"product": products})
