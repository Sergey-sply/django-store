from django.core.paginator import Paginator
from django.shortcuts import render, get_list_or_404

from products.models import Products

def catalog(request, category_slug):
    """For displaying all products"""
    
    page = request.GET.get('page', 1)

    if category_slug == 'all':
        products = Products.objects.all() # get all prod from bd 'products'
    else:
        products = get_list_or_404(Products.objects.filter(category__slug=category_slug))
        
    paginator = Paginator(products, per_page=3)
    current_page = paginator.page(int(page))

    context = {
        "title": "Home - Каталог",
        "products": current_page,
        "slug_url": category_slug,
    }

    return render(request, "products/catalog.html", context)


def product(request, product_slug):
    """For displaying a certain product"""

    product = Products.objects.get(slug=product_slug)

    context = {
        'product': product,
    }

    return render(request, "products/product.html", context=context)
