from abc import ABC

from project.animals.animal import Mammal
from project.food import Vegetable, Meat, Fruit


class Mouse(Mammal):

    def make_sound(self):
        return "Squeak"

    @property
    def eaten_food(self):
        return [Vegetable, Fruit]

    @property
    def increase_weight(self):
        return 0.10


class Dog(Mammal):

    def make_sound(self):
        return "Woof!"

    @property
    def eaten_food(self):
        return [Meat]

    @property
    def increase_weight(self):
        return 0.40

class Cat(Mammal):

    def make_sound(self):
        return "Meow"

    @property
    def eaten_food(self):
        return [Vegetable, Meat]

    @property
    def increase_weight(self):
        return 0.30


class Tiger(Mammal):

    def make_sound(self):
        return "ROAR!!!"

    @property
    def eaten_food(self):
        return [Meat]

    @property
    def increase_weight(self):
        return 1.00


