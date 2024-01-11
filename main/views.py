from django.http import HttpResponse
from django.shortcuts import render

from products.models import Categories


def index(request):

    context: dict = {
        'title': 'Home', 
        'content': 'Главная страница - Home',
        }

    return render(request, 'main/index.html', context)


def about(request):
    context: dict = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Тестовый текст для проверки работы шаблона йцукенгшщзхъфывапролджэячсмитьбю'
    }

    return render(request, 'main/about.html', context)
