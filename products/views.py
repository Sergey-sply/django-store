from django.shortcuts import render, get_object_or_404

from products.models import Products

def catalog(request, category_slug):
    """For displaying all products"""

    if category_slug == 'all':
        products = Products.objects.all() # get all prod from bd 'products'
    else:
        products = get_object_or_404(Products.objects.filter(category__slug=category_slug))
        
    context = {
        "title": "Home - Каталог",
        "products": products,
    }

    return render(request, "products/catalog.html", context)


def product(request, product_slug):
    """For displaying a certain product"""

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, "products/product.html", context=context)
