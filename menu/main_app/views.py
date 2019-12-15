from django.shortcuts import render

from main_app.models import Allergen, Category


def index(request):
    return render(request, 'main_app/index.html', {
        'allergens': Allergen.objects.all(),
        'categories': Category.objects.all(),
    })


def order(request):
    return render(request, 'main_app/order.html')
