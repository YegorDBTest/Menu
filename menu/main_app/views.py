from django.shortcuts import render

from main_app.models import Allergen, Category
from main_app.serializers import DishSerializer


def index(request):
    '''
    Страница с меню.
    Даные о блюдах запрашиваются через API.
    '''

    return render(request, 'main_app/index.html', {
        'categories': Category.objects.all(),
        'serializer': DishSerializer(),
    })


def order(request):
    '''
    Страница с заказом.
    Даные о блюдах запрашиваются через API.
    '''

    return render(request, 'main_app/order.html')
