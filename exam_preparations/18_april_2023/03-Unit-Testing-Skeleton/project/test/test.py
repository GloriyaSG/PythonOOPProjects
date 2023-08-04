from project.robot import Robot
from unittest import TestCase, main

class TestRobot(TestCase):

    def setUp(self):
        self.robot = Robot("ABC", "Military", 10, 30)

    def test_initialisation(self):
        self.assertEqual(self.robot.robot_id, "ABC")
        self.assertEqual(self.robot.category, "Military")
        self.assertEqual(self.robot.available_capacity, 10)
        self.assertEqual(self.robot.price, 30)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])
        self.assertEqual(['Military', 'Education', 'Entertainment', 'Humanoids'], self.robot.ALLOWED_CATEGORIES)
        self.assertEqual(self.robot.PRICE_INCREMENT, 1.5)


    def test_category_setter(self):
        category = ['Military', 'Education', 'Entertainment', 'Humanoids']
        with self.assertRaises(ValueError) as ex:
            self.robot.category = "Test"
        self.assertEqual(f"Category should be one of '{category}'", str(ex.exception))
        self.assertEqual(self.robot.category, "Military")

    def test_price_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.robot.price = -1
        self.assertEqual(self.robot.price, 30)
        self.assertEqual("Price cannot be negative!", str(ex.exception))

    def test_update_method(self):
        self.robot.software_updates = [20,30,40]
        res = self.robot.update(1, 10)
        self.assertEqual("Robot ABC was not updated.", res)

        self.robot.available_capacity = 1
        res = self.robot.update(1,10)
        self.assertEqual("Robot ABC was not updated.", res)

        self.robot.software_updates = []
        self.robot.available_capacity = 30
        res = self.robot.update(2, 10)
        self.assertEqual("Robot ABC was updated to version 2.", res)

    def test_upgrade_method(self):
        self.robot.hardware_upgrades = ["USB", "Flash", "Mic"]
        res = self.robot.upgrade("USB", 12)
        self.assertEqual("Robot ABC was not upgraded.", res)

        res = self.robot.upgrade("C port", 15)
        self.assertEqual("Robot ABC was upgraded with C port.", res)
        self.assertEqual(["USB", "Flash", "Mic", "C port"], self.robot.hardware_upgrades)
        self.assertEqual(self.robot.price, 52.50)


    def test_greater_method(self):
        other = Robot("ABCD", "Military", 10, 20)
        res = self.robot.__gt__(other)
        self.assertEqual('Robot with ID ABC is more expensive than Robot with ID ABCD.', res)

        other = Robot("ABCD", "Military", 10, 30)
        res = self.robot.__gt__(other)
        self.assertEqual("Robot with ID ABC costs equal to Robot with ID ABCD.", res)

        other = Robot("ABCD", "Military", 10, 50)
        res = self.robot.__gt__(other)
        self.assertEqual("Robot with ID ABC is cheaper than Robot with ID ABCD.", res)

if __name__ == "__main__":
    main()