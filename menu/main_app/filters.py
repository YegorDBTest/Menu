from django import forms
from django.core.validators import validate_comma_separated_integer_list

from django_filters import rest_framework as filters
from django_filters import Filter

from main_app.models import Dish


class IntListField(forms.Field):
    def to_python(self, value):
        if not value:
            return []
        validate_comma_separated_integer_list(value)
        return [int(item) for item in value.split(',')]


class NumberListFilter(Filter):
    field_class = IntListField


class DishFilterSet(filters.FilterSet):
    ids = NumberListFilter(field_name="id", lookup_expr='in')

    class Meta:
        model = Dish
        fields = ['ids']
