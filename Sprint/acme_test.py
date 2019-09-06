"""
Test
"""

import unittest
import random
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)


"""
Test default num products and legal names
"""


class AcmeProductTests(unittest.TestCase):
    def test_default_num_products(self):
        num = generate_products()
        self.assertEqual(len(num), 30)

    def test_legal_names(self):
        gp = generate_products()
        names = [x.name for x in gp]
        for name in names:
            self.assertEqual(len(name.split(' ')), 2)
        for name in names:
            new_name = name.split(' ')
            ads = new_name[0]
            nns = new_name[1]
            self.assertIn(ads, ADJECTIVES)
            self.assertIn(nns, NOUNS)

if __name__ == '__main__':
    unittest.main()
