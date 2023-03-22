import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'restauraunt.settings')


django.setup()
from rango.models import Dish

def populate():
    data = [
        {'dishname': 'KHAO SAWY',
         'type': 'Rice & Noodle',
         'price': '9.8',
         'description': 'A fragrant and creamy coconut curry noodle soup, popular in Northern Thailand. Served with tender meat, crunchy toppings and a squeeze of lime.'},
    ]

    for dish_data in data:
        dish = Dish.objects.get_or_create(
            dishname=dish_data['dishname'],
            type=dish_data['type'],
            price=dish_data['price'],
            description=dish_data['description']
        )[0]
        dish.save()

if __name__ == '__main__':
    print('Populating the database... Please wait.')
    populate()
    print('Database population complete.')

