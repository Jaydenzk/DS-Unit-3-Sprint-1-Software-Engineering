"""
Class for Acme
"""

import random
import numpy as np


class Product:

    """
    Class to model product
    """

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

        """
        Determination of stealaility is given price/a_weight 
        when x<0.5 print "Not so stealable"
        and 0.5<x<1 print "Kinda stealable"
        otherwise print "Very stealable"
        """

        if x < 0.5:
            return "Not so stealable..."
        elif x >= 0.5 and x < 1:
            return "Kinda stealable..."
        else:
            return "Very stealable!"


def explode(self):

    """
    Determination of explode is given flammability/weight
    when y<10 print "...fizzle"
    and 10<y<50 print "...boom"
    otherwise print "...BABOOM"
    """

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

    """
    Class to model BoxingGlove and default weight change to 10
    """

    random = random.randint(1000000, 9999999)


def __init__(self, name, price=10, weight=10, flammability=0.5,
             identifier=random):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier


def explode(self):
    """If boxing glove override, explode statement always print "it's a glove" """
    print("...it's a glove")


def punch(self):
    """Determination of punch is given glove weight"""
    if self.weight < 5:
        print("That tickles.")
    elif self.weight < 15:
        print("Hey that hurt!")
    else:
        print("OUCH!")
