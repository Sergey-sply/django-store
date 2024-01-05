from django.shortcuts import render

def catalog(request):
    '''For displaying all products'''

    return render(request, 'products/catalog.html')

def product(request):
    '''For displaying a certain product'''

    return render(request, 'products/product.html')
