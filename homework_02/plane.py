"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02 import exceptions

class Plane(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, cargo=None, max_cargo=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = cargo
        self.max_cargo = max_cargo

    def load_cargo(self, val_cargo):
        if self.cargo + val_cargo > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo = self.cargo + val_cargo

#cargo и max_cargo