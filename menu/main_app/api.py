from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response

from main_app.serializers import DishSerializer


@api_view(['POST'])
@parser_classes([MultiPartParser])
def create_dish(request):
    '''
    Создание блюда.
    Данные: форма модели блюда.
    '''

    serializer = DishSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
