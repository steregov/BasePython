"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class CarException(BaseException):
    pass

class LowFuelError(CarException):
    pass

class NotEnoughFuel(CarException):
    pass

class CargoOverload(CarException):
    pass