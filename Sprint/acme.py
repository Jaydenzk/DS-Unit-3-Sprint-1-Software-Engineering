"""
Class for Acme
"""

import random
import numpy as np


class Product:

    random = random.randint(1000000, 9999999)

    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


"""
stealability
"""


def stealability(self):
        x = (self.price)/(self.weight)

        if x < 0.5:
            return "Not so stealable..."
        elif x >= 0.5 and x < 1:
            return "Kinda stealable..."
        else:
            return "Very stealable!"


def explode(self):
        y = (self.flammability)*(self.weight)

        if y < 10:
            return "...fizzle."
        elif y >= 10 and x < 50:
            return "...boom"
        else:
            return "...BABOOM"


"""
Subclass BoxingGlove
"""


class BoxingGlove(Product):
    import random
    random = random.randint(1000000, 9999999)


def __init__(self, name, price=10, weight=10, flammability=0.5,
             identifier=random):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


def explode(self):
        print("...it's a glove")


def punch(self):
        if self.weight < 5:
            print("That tickles.")
        elif self.weight < 15:
            print("Hey that hurt!")
        else:
            print("OUCH!")
