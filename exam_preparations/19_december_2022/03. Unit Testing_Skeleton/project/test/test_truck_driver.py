from project.truck_driver import TruckDriver
from unittest import TestCase, main

class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("TestTruck", 10)

    def test_initalization(self):
        self.assertEqual("TestTruck", self.driver.name)
        self.assertEqual(10, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.driver.earned_money = -1
        self.assertEqual("TestTruck went bankrupt.", str(ex.exception))

        self.driver.earned_money = 100
        self.assertEqual(100, self.driver.earned_money)

    def test_adding_cargo_offer(self):

        offer = self.driver.add_cargo_offer("TestCargo", 100)
        res = "Cargo for 100 to TestCargo was added as an offer."
        self.assertEqual(res, offer)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("TestCargo", 100)
        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_drive_best_cargo_offer(self):

        res = self.driver.drive_best_cargo_offer()
        self.assertEqual("There are no offers available.", res)

        self.driver.add_cargo_offer("TestCargo", 100)
        self.driver.add_cargo_offer("TestCargo2", 200)
        self.driver.add_cargo_offer("TestCargo3", 300)
        res = self.driver.drive_best_cargo_offer()
        self.assertEqual("TestTruck is driving 300 to TestCargo3.", res)

        self.assertEqual(self.driver.earned_money, 2980)
        self.assertEqual(self.driver.miles, 300)



    def test_check_for_activities(self):
        self.driver.earned_money = 500
        self.driver.check_for_activities(250)
        self.assertEqual(480, self.driver.earned_money)

        self.driver.earned_money = 1000
        self.driver.check_for_activities(1000)
        self.assertEqual(875, self.driver.earned_money)

        self.driver.earned_money = 1500
        self.driver.check_for_activities(1500)
        self.assertEqual(835, self.driver.earned_money)

        self.driver.earned_money = 20000
        self.driver.check_for_activities(10000)
        self.assertEqual(8250, self.driver.earned_money)

    def test_if_repr_returns_correct(self):
        rep = repr(self.driver)
        res = "TestTruck has 0 miles behind his back."
        self.assertEqual(rep, res)


















if __name__ == '__main__':
    main()