"""
Class for Acme
"""

import random
import numpy as np


class Product:

    """
    Class to model product which everything goes here
    
    Product:
    -name (string with no default)
    -price (integer with default value 10)
    -weight (integer with default value 20)
    -flammability (float with default value 0.5)
    -identifier (integer, automatically genererated as a random (uniform)
    number anywhere from 1000000 to 9999999, includisve).
    
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
        
        """
        Determination of stealaility(self) is given price/a_weight
        
        if the ratio:
        less than 0.5 
        return "Not so stealable"
        
        greater than 0.5 but less than 1 
        return "Kinda stealable"
        
        otherwise return "Very stealable"
        
        """
    x = (self.price)/(self.weight)

    if x < 0.5:
        return "Not so stealable..."
    elif x >= 0.5 and x < 1:
        return "Kinda stealable..."
    else:
        return "Very stealable!"


def explode(self):

    """
    Determination of explode is given flammability/weight
    if the ratio:
    less than 10 
    return "...fizzle"
    
    greater than 10 but less than 50 
    return "...boom"
    
    otherwise return "...BABOOM"
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
    If override the explode method to always "...it's a glove."
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
    """
    Determination of punch is given glove weight
    
    If the weight: 
    less than 5
    return "That tickles."
    
    greater than 5 but less than 15
    return "Hey that hurt!"
    
    greater than 15
    return "OUCH!"
    """
    if self.weight < 5:
        print("That tickles.")
    elif self.weight < 15:
        print("Hey that hurt!")
    else:
        print("OUCH!")
