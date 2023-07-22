from abc import ABC

from project.animals.animal import Bird
from project.food import Meat, Vegetable, Seed, Fruit


class Owl(Bird):


    def make_sound(self):
        return "Hoot Hoot"

    @property
    def eaten_food(self):
        return [Meat]

    @property
    def increase_weight(self):
        return 0.25


class Hen(Bird):

    def make_sound(self):
        return "Cluck"

    @property
    def eaten_food(self):
        return [Meat, Vegetable, Seed, Fruit]

    @property
    def increase_weight(self):
        return 0.35


