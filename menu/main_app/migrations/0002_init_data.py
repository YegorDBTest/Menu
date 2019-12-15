from django.contrib.auth.models import User
from django.db import migrations


allergens_names = [f'Аллерген{i}' for i in range(1, 6)]
categories_names = [f'Категория{i}' for i in range(1, 11)]


def get_models(apps):
    return (
        apps.get_model("main_app", "Allergen"),
        apps.get_model("main_app", "Category")
    )


def create_data(apps, schema_editor):
    Allergen, Category = get_models(apps)
    User.objects.create_superuser('qwerty', '', 'qwerty')
    Allergen.objects.bulk_create([Allergen(name=n) for n in allergens_names])
    Category.objects.bulk_create([Category(name=n) for n in categories_names])


def delete_data(apps, schema_editor):
    Allergen, Category = get_models(apps)
    User.objects.filter(username='qwerty').delete()
    Allergen.objects.filter(name__in=allergens_names).delete()
    Category.objects.filter(name__in=categories_names).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_data, delete_data),
    ]
