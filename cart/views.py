from django.shortcuts import render, redirect, reverse
from product.views import all_products
from django.contrib import auth, messages

# Create your views here.

def view_cart(request):
    """Renders everything in the cart"""
    # cartcontent = request.session.get('cart' , {})
    # if not cartcontent:
    #     messages.warning(request, 'There are no items in your cart')
    #     return render(request, "cart.html")
    # else:
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add quantity of the specified product of the cart"""
    quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('product'))


def adjust_cart(request, id):
    """Adjust the quantity of a specified product by a specified amount"""
    print(request.POST)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
        # size = request.POST.get('size_choices')
        # cart = request.session.get('cart', {})
        # request.session['cart']['size'] = size
    else:
        cart.pop(id)


    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


