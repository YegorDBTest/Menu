from django.db import models


class Allergen(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField('Название', max_length=255)
    squirrels = models.DecimalField('Белки', max_digits=9, decimal_places=2)
    fats = models.DecimalField('Жиры', max_digits=9, decimal_places=2)
    carbohydrates = models.DecimalField('Углеводы', max_digits=9, decimal_places=2)
    energy = models.PositiveIntegerField('Энергетическая ценность')
    price = models.DecimalField('Цена', max_digits=9, decimal_places=2)
    picture = models.ImageField('Фото', upload_to='dishes/%Y/%m/%d', max_length=255)
    allergens = models.ManyToManyField(Allergen)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
