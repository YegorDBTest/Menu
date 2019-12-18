from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from main_app.models import Dish
from main_app.serializers import DishSerializer
from main_app.utils import aggregate_dishes_data, aggregate_dishes_data_with_total


@api_view(['GET'])
def get_dishes(request):
    '''
    Получение информации о блюдах.
    Get параметры:
    - ids (id блюд через запятую);
    - tn (необходимость передачи сводных значений по блюдам).
    Если id блюд не переданы - отдается информация о всех блюдах.
    Если tn равен 1 - помимо данных о блюдах отдается информация
    о суммах белков, жиров, углеводов, енергии и цен всех блюд,
    а также о всех аллергенах содержащихся в блюдах.
    '''

    dishes_ids = request.query_params.get('ids', None)
    total_needed = request.query_params.get('tn', None) == '1'

    additional_filter = {}
    if dishes_ids:
        additional_filter['id__in'] = dishes_ids.split(',')

    dishes = (
        Dish.objects
        .filter(**additional_filter)
        .select_related('category')
        .prefetch_related('allergens')
    )

    data = (
        aggregate_dishes_data_with_total(dishes)
        if total_needed else
        aggregate_dishes_data(dishes)
    )

    return Response(data, status=status.HTTP_200_OK)


@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_dish(request):
    '''
    Создание блюда.
    Данные: форма, основанная на модели блюда.
    '''

    serializer = DishSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
