
"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02.engine import Engine

class Car(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine

    def set_engine(self, add_engine):
        if isinstance(add_engine, Engine):
            self.engine = add_engine
