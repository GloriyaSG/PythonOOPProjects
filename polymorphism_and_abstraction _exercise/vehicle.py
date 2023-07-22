from abc import abstractmethod, ABC


class Vehicle(ABC):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass

class Car(Vehicle):
    increase_per_km = 0.9


    def drive(self, distance):
        consumption = (self.fuel_consumption + Car.increase_per_km) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel

class Truck(Vehicle):
    increase_per_km = 1.6
    TRUCK_TANK = 0.95
    def drive(self, distance):
        consumption = (self.fuel_consumption + Truck.increase_per_km) * distance

        if self.fuel_quantity >= consumption:
            self.fuel_quantity -= consumption

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.TRUCK_TANK

car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)





