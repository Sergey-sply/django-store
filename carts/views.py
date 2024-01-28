from django.shortcuts import redirect, render

from carts.models import Cart
from products.models import Products

def cart_add(request):
    
    product_id = request.POST.get("product_id")
    product = Products.objects.get(id=product_id)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)

        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)
            
    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    ...

def cart_remove(request, cart_id):

    cart = Cart.objects.get(id=cart_id)
    cart.delete()

    return redirect(request.META['HTTP_REFERER'])

