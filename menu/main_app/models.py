from django.db import models


class Allergen(models.Model):
    class Meta:
        verbose_name = 'Аллерген'
        verbose_name_plural = 'Аллергены'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    name = models.CharField('Название', max_length=255)

    def __str__(self):
        return self.name


class Dish(models.Model):
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

    name = models.CharField('Название', max_length=255)
    squirrels = models.DecimalField('Белки, г.', max_digits=9, decimal_places=2)
    fats = models.DecimalField('Жиры, г.', max_digits=9, decimal_places=2)
    carbohydrates = models.DecimalField('Углеводы, г.', max_digits=9, decimal_places=2)
    energy = models.PositiveIntegerField('Энергетическая ценность, кКал.')
    price = models.DecimalField('Цена, руб.', max_digits=9, decimal_places=2)
    picture = models.ImageField('Фото', upload_to='dishes/%Y/%m/%d', max_length=255)
    allergens = models.ManyToManyField(Allergen, verbose_name='Аллергены')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
