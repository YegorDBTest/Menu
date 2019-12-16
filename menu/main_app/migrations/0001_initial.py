from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={'verbose_name': 'Аллерген', 'verbose_name_plural': 'Аллергены'},
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('squirrels', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Белки, г.')),
                ('fats', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Жиры, г.')),
                ('carbohydrates', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Углеводы, г.')),
                ('energy', models.PositiveIntegerField(verbose_name='Энергетическая ценность, кКал.')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена, руб.')),
                ('picture', models.ImageField(max_length=255, upload_to='dishes/%Y/%m/%d', verbose_name='Фото')),
                ('allergens', models.ManyToManyField(to='main_app.Allergen', verbose_name='Аллергены')),
                ('category', models.ForeignKey(to='main_app.Category', verbose_name='Категория', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={'verbose_name': 'Блюдо', 'verbose_name_plural': 'Блюда'},
        ),
    ]
