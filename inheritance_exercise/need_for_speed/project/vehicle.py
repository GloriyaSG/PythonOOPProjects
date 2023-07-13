class Vehicle:

    DEFAULT_FUEL_CONSUMPTION: float = 1.25

    def __init__(self, fuel:float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        consumption = self.fuel_consumption * kilometers
        if self.fuel >= consumption:
            self.fuel -= consumption


