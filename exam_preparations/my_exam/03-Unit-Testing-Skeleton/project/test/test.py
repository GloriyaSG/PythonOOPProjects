from project.second_hand_car import SecondHandCar

from unittest import TestCase, main

class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car = SecondHandCar("Test", "Testov", 200, 100)

    def test_initialization(self):
        self.assertEqual("Test", self.car.model)
        self.assertEqual("Testov", self.car.car_type)
        self.assertEqual(200, self.car.mileage)
        self.assertEqual(100, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.car.price = 0
        self.assertEqual("Price should be greater than 1.0!", str(ex.exception))
        self.assertEqual(100, self.car.price)

    def test_mileage_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 100
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ex.exception))
        self.assertEqual(200, self.car.mileage)

        with self.assertRaises(ValueError) as ex:
            self.car.mileage = 60
        self.assertEqual("Please, second-hand cars only! Mileage must be greater than 100!", str(ex.exception))
        self.assertEqual(200, self.car.mileage)

    def test_set_promotional_price_method(self):
        with self.assertRaises(ValueError) as ex:
            self.car.set_promotional_price(200)
        self.assertEqual("You are supposed to decrease the price!", str(ex.exception))

        res = self.car.set_promotional_price(80)
        self.assertEqual("The promotional price has been successfully set.", res)
        self.assertEqual(80, self.car.price)

    def test_need_repair_method(self):
        res = self.car.need_repair(80, "Turbine")
        self.assertEqual('Repair is impossible!', res)

        res = self.car.need_repair(30, "Turbine")
        self.assertEqual('Price has been increased due to repair charges.', res)
        self.assertEqual(130, self.car.price)
        self.assertEqual(["Turbine"], self.car.repairs)

    def test_gt_method(self):
        other = SecondHandCar("Test1", "Testov1", 200, 100)
        res = self.car.__gt__(other)
        self.assertEqual('Cars cannot be compared. Type mismatch!', res)

        other = SecondHandCar("Test1", "Testov", 200, 50)
        res = self.car.__gt__(other)
        self.assertTrue(res)

        other = SecondHandCar("Test1", "Testov", 200, 300)
        res = self.car.__gt__(other)
        self.assertFalse(res)

    def test_str_method(self):
        res = """Model Test | Type Testov | Milage 200km
Current price: 100.00 | Number of Repairs: 0"""
        self.assertEqual(str(self.car), res)

        self.car.repairs = ["Test1", "Test2", "Test3", "Test4"]
        res = """Model Test | Type Testov | Milage 200km
Current price: 100.00 | Number of Repairs: 4"""
        self.assertEqual(str(self.car), res)









if __name__ == '__main__':
    main()
