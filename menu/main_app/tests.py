from decimal import Decimal
from PIL import Image
from tempfile import NamedTemporaryFile

from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from main_app.models import Allergen, Category


class CreateDishAPITestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.url = reverse('create-dish')
        cls.allergen1 = Allergen.objects.create(name='Allergen1')
        cls.allergen2 = Allergen.objects.create(name='Allergen2')
        cls.category = Category.objects.create(name='Category')

    @property
    def _picture_file(self):
        image = Image.new('RGB', (100, 100))
        tmp_file = NamedTemporaryFile(suffix='.jpg')
        image.save(tmp_file)
        tmp_file.seek(0)
        return tmp_file

    def _get_data(self, **kwargs):
        return {
            'name': kwargs.get('name') or 'Dish',
            'squirrels': kwargs.get('squirrels') or '12.02',
            'fats': kwargs.get('fats') or '25.71',
            'carbohydrates': kwargs.get('carbohydrates') or '56.2',
            'energy': kwargs.get('energy') or 100,
            'price': kwargs.get('price') or '246.03',
            'picture': kwargs.get('picture') or self._picture_file,
            'allergens': kwargs.get('allergens') or [self.allergen1.name, self.allergen2.name],
            'category': kwargs.get('category') or self.category.id
        }

    def _post_data(self, data):
        return self.client.post(self.url, data, format='multipart')

    def test_create(self):
        data = self._get_data()
        response = self._post_data(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_with_empty_allergens(self):
        data = self._get_data(name='Dish2', allergens=[])
        response = self._post_data(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_without_allergens(self):
        data = self._get_data(name='Dish3')
        del data['allergens']
        response = self._post_data(data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_wrong_data(self):
        wrong_data = {
            'squirrels': '9876543210',
            'fats': 'qwerty',
            'carbohydrates': True,
            'energy': '%$#',
            'price': 113.09874632,
            'picture': b'123',
            'allergens': [56, True],
            'category': 'asdfgh'
        }

        for key, value in wrong_data.items():
            data = self._get_data(name=f'WrongDish{key}', **{key: value})
            response = self._post_data(data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_empty_required_data(self):
        keys = [
            'name',
            'squirrels',
            'fats',
            'carbohydrates',
            'energy',
            'price',
            'picture',
            'category'
        ]

        for key in keys:
            data = self._get_data(name=f'EmptyDish{key}')
            del data[key]
            response = self._post_data(data)
            self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
