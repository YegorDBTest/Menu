from decimal import Decimal


def get_dish_data(dish):
    return {
        'category': dish.category.id,
        'id': dish.id,
        'name': dish.name,
        'picture': dish.picture.url,
        'squirrels': dish.squirrels,
        'fats': dish.fats,
        'carbohydrates': dish.carbohydrates,
        'energy': dish.energy,
        'price': dish.price,
        'allergens': dish.allergens.values_list('name', flat=True)
    }


def aggregate_dishes_data(dishes):
    return {
        'dishes': [get_dish_data(dish) for dish in dishes],
    }


def aggregate_dishes_data_with_total(dishes):
    data = {
        'dishes': [],
        'total': {
            'price': Decimal(0),
            'allergens': set(),
        },
    }

    for dish in dishes:
        dish_data = get_dish_data(dish)
        data['total']['price'] += dish_data['price']
        data['total']['allergens'] |= set(dish_data['allergens'])
        data['dishes'].append(dish_data)

    return data
