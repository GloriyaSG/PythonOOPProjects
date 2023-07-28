from unittest import TestCase, main

#from car_manager import Car


class TestCar(TestCase):
    def setUp(self):
        self.car = Car('Mercedes','C-Class',7,10)

    def test_initialize(self):
        self.assertEqual(self.car.make, 'Mercedes')
        self.assertEqual(self.car.model, 'C-Class')
        self.assertEqual(self.car.fuel_consumption, 7)
        self.assertEqual(self.car.fuel_capacity, 10)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_making_invalid_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_invalid_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_invalid_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_invalid_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_invalid_new_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))


    def test_invalid_refuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_greater_amount(self):
        self.car.fuel_amount = 9
        self.car.refuel(2)
        self.assertEqual(10, self.car.fuel_amount)

    def test_drive_with_greater_than_needed_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == '__main__':
    main()
