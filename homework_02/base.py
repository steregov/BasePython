from abc import ABC
from homework_02 import exceptions

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    pass

    def start(self):
        if self.started:
            self.started = False
        else:
            if self.fuel > 0:
                self.started = True
            else:
                raise exceptions.LowFuelError

    def move(self, distance=0):
        fuel_need = distance/100*self.fuel_consumption
        if fuel_need <= self.fuel:
            self.fuel = self.fuel-fuel_need
        else:
            raise exceptions.NotEnoughFuel
'''
Vehicle_1 = Vehicle(1500, False, 10, 7)
Vehicle_1.fuel = 5
print(vars(Vehicle_1))
Vehicle_1.fuel = 10
Vehicle_1.start()
print(vars(Vehicle_1))
Vehicle_1.move(105)
print(vars(Vehicle_1))
Vehicle_1.move(30)
print(vars(Vehicle_1))
'''