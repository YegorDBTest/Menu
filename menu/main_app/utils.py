from decimal import Decimal


def aggregate_dishes_data(dishes):
    return {
        'dishes': dishes,
    }


def aggregate_dishes_data_with_total(dishes):
    data = {
        'dishes': dishes,
        'total': {
            'price': Decimal(0),
            'allergens': set(),
        },
    }

    for dish in dishes:
        data['total']['price'] += Decimal(dish['price'])
        data['total']['allergens'] |= set(dish['allergens'])

    return data
