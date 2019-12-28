from django.views.generic.base import TemplateView

from main_app.models import Category
from main_app.serializers import DishSerializer


class IndexView(TemplateView):
    '''
    Страница с меню.
    Даные о блюдах запрашиваются через API.
    '''

    template_name = 'main_app/index.html'
    http_method_names = ['get']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'categories': Category.objects.all(),
            'serializer': DishSerializer(),
        })
        return context


class OrderView(TemplateView):
    '''
    Страница с заказом.
    Даные о блюдах запрашиваются через API.
    '''

    template_name = 'main_app/order.html'
    http_method_names = ['get']
