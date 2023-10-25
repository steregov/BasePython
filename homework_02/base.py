from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance=0):
        fuel_need = distance*self.fuel_consumption
        if fuel_need <= self.fuel:
            self.fuel = self.fuel-fuel_need
        else:
            raise exceptions.NotEnoughFuel

'''
Vehicle_1 = Vehicle( 1500, 10, 0.1)
Vehicle_1.fuel = 10
print(vars(Vehicle_1))
Vehicle_1.move(70)
print(vars(Vehicle_1))
'''