
"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base, engine

class Car(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, add_engine: object):
        if isinstance(add_engine, engine):
            self.engine = add_engine
