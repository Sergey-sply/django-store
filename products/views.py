from django.shortcuts import render

from products.models import Products

def catalog(request):
    """For displaying all products"""

    products = Products.objects.all() # get all prod from bd 'products'

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
