import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','project.settings')

import django
django.setup()

from django_seed import Seed

seeder = Seed.seeder()

from shop.models import Product, OrderHeader, OrderLine
import random

flowers = ['African Daisy', 'Begonia', 'Calla Lily', 'Daffodil', 'English Bluebell',
    'Foxglove', 'Gladiolus', 'Hosta', 'Iris', 'Jasmine', 'Kaffir Lily', 'Lily',
    'Mimosa', 'Narcissus', 'Orchid', 'Peony', 'Quince', 'Rose', 'Silene', 'Tiger Flower',
    'Urn Plant', 'Viola', 'Waterlily', 'Xeranthemum', 'Yellow Bell', 'Zephyranthes']
seeder.add_entity(Product, 30, {
    'name': lambda x: random.choice(flowers) + ' ' + str(random.randint(1, 10000)),
    'price': lambda x: random.randint(1, 1000) / 100
})

seeder.add_entity(OrderHeader, 50, {
    'total': 0.0
})

seeder.add_entity(OrderLine, 200, {
    'quantity': lambda x: random.randint(1, 100),
    'subtotal': 0.0
})

inserted_pks = seeder.execute()

for line in OrderLine.objects.all():
    product = Product.objects.get(id=line.product.id)
    line.subtotal = line.quantity * product.price
    line.save()

for order in OrderHeader.objects.all():
    lines = OrderLine.objects.filter(order_id=order.id)
    total_amount = 0
    for line in lines:
        total_amount += line.subtotal
    order.total = total_amount
    order.save()
