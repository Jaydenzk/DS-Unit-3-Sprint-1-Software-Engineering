"""
acme_report
"""

from acme import Product
import random


ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(N=30):
    """Generate products default n=30, random and return it as list"""
    products = []

    for i in range(N):
        product = Product(
            name=random.choice(ADJECTIVES) + " " + random.choice(NOUNS),
            price=random.randint(5, 100),
            weight=random.randint(5, 100),
            flammability=random.uniform(0.0, 2.5)
            )
        products.append(product)
    return products


def inventory_report(products):
    """Inventory report prints a summary of products"""
    print('ACME INVENTORY REPORT\\N')

    names = len(set([x.name for x in products]))

    def mean(l):
        return sum(l)/len(l)

    a_price = mean([x.price for x in products])
    a_weight = mean([x.weight for x in products])
    a_flam = mean([x.flammability for x in products])

    print('Average price: ', a_price)
    print('\nAverage weight:', a_weight)
    print('\nAverage flammability:', a_flam)

    return

if __name__ == '__main__':
    print(inventory_report(generate_products()))
