from abc import ABC

class Vehicle(ABC):
    def __init__(self, weight=0, started=False, fuel=0, fuel_consumption=0):
        self.weight = weight
        self.started = started
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
    pass

    def start(self):
        if not self.started and self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance=0):
        fuel_need = distance/100*self.fuel_consumption
        if fuel_need <= self.fuel:
            self.fuel = self.fuel-fuel_need
        else:
            raise NotEnoughFuel

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