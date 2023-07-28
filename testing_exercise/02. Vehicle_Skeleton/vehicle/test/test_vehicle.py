from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(10.5, 12.5)

    def test_initializing_config(self):
        self.assertEqual(self.vehicle.fuel, 10.5)
        self.assertEqual(self.vehicle.capacity, 10.5)
        self.assertEqual(self.vehicle.horse_power, 12.5)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_driving_with_correct_value(self):
        self.vehicle.drive(5)
        self.assertEqual(4.25, self.vehicle.fuel)

    def test_driving_with_incorrect_value(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(677)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_with_more_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(20)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_correct_value(self):
        self.vehicle.fuel = 1.5
        self.vehicle.refuel(7.5)
        self.assertEqual(9, self.vehicle.fuel)


    def test_str_method(self):
        result = f"The vehicle has 12.5 " \
               f"horse power with 10.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(result, str(self.vehicle))

if __name__ == '__main__':
    main()