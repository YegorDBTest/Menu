from rest_framework import serializers

from main_app.models import Dish


class DishSerializer(serializers.ModelSerializer):
    allergens = serializers.StringRelatedField(many=True, required=False)

    class Meta:
        model = Dish
        fields = "__all__"
