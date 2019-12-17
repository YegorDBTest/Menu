from decimal import Decimal


def aggregate_dishes_data(dishes):
    return {
        'dishes': [{
                'category_id': dish.category.id,
                'id': dish.id,
                'squirrels': dish.squirrels,
                'fats': dish.fats,
                'carbohydrates': dish.carbohydrates,
                'energy': dish.energy,
                'price': dish.price,
                'allergens': dish.allergens.values_list('name', flat=True)
            }
            for dish in dishes
        ],
    }


def aggregate_dishes_data_with_total(dishes):
    data = {
        'dishes': [],
        'total': {
            'squirrels': Decimal(0),
            'fats': Decimal(0),
            'carbohydrates': Decimal(0),
            'energy': 0,
            'price': Decimal(0),
            'allergens': set(),
        },
    }

    for dish in dishes:
        dish_data = {
            'category_id': dish.category.id,
            'id': dish.id,
        }

        for key in ('squirrels', 'fats', 'carbohydrates', 'energy', 'price'):
            value = getattr(dish, key)
            dish_data[key] = value
            data['total'][key] += value

        allergens = set(dish.allergens.values_list('name', flat=True))
        dish_data['allergens'] = allergens
        data['total']['allergens'] |= allergens

        data['dishes'].append(dish_data)

    return data
