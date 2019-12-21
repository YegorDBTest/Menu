from rest_framework import serializers

from main_app.models import Allergen, Dish


class DishSerializer(serializers.ModelSerializer):
    allergens = serializers.SlugRelatedField(
        many=True,
        required=False,
        queryset=Allergen.objects.all(),
        slug_field='name'
    )

    class Meta:
        model = Dish
        fields = (
            'name',
            'squirrels',
            'fats',
            'carbohydrates',
            'energy',
            'price',
            'picture',
            'allergens',
            'category'
        )

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['id'] = instance.id
        return ret
