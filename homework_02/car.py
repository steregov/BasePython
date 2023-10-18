
"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base

class Car(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, add_engine):
        self.engine = add_engine
