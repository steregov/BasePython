"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02 import base
from homework_02 import exceptions

class Plane(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, max_cargo=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, val_cargo):
        if self.cargo + val_cargo > self.max_cargo:
            raise exceptions.CargoOverload
        else:
            self.cargo = self.cargo + val_cargo

    def remove_all_cargo(self):
        prev_cargo = self.cargo
        self.cargo = 0
        return prev_cargo

#cargo и max_cargo