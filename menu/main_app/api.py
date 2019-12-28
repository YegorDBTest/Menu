from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.parsers import MultiPartParser

from main_app.models import Dish
from main_app.filters import DishFilterSet
from main_app.serializers import DishSerializer
from main_app.utils import aggregate_dishes_data, aggregate_dishes_data_with_total


class GetDishes(generics.ListAPIView):
    '''
    Получение информации о блюдах.
    Get параметры:
    - ids (id блюд через запятую);
    - tn (необходимость передачи сводных значений по блюдам).
    Если id блюд не переданы - отдается информация о всех блюдах.
    Если tn равен 1 - помимо данных о блюдах отдается информация
    о сумме цен всех блюд, а также о всех аллергенах, содержащихся в блюдах.
    '''

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = DishFilterSet
    http_method_names = ['get']

    def _response_data_aggregate(self, request, response):
        total_needed = request.query_params.get('tn', None) == '1'
        response.data = (
            aggregate_dishes_data_with_total(response.data)
            if total_needed else
            aggregate_dishes_data(response.data)
        )
        return response

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return self._response_data_aggregate(request, response)


class CreateDish(generics.CreateAPIView):
    '''
    Создание блюда.
    Данные: форма, основанная на модели блюда.
    '''

    serializer_class = DishSerializer
    parser_classes = [MultiPartParser]
    http_method_names = ['post']
