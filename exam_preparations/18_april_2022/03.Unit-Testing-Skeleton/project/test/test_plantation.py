from project.plantation import Plantation

from unittest import TestCase, main


class TestPlantation(TestCase):

    def setUp(self):
        self.plantation = Plantation(2)

    def test_initalization(self):
        self.assertEqual(self.plantation.size, 2)
        self.assertEqual(self.plantation.plants, {})
        self.assertEqual(self.plantation.workers, [])

    def test_size_setter(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(ex.exception))
        self.assertEqual(self.plantation.size, 2)
    def test_if_hire_worker_raises_exception(self):
        self.plantation.workers = ["Test", "Test2"]
        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker("Test")
        self.assertEqual("Worker already hired!", str(ex.exception))


        result = self.plantation.hire_worker("Test3")
        self.assertEqual("Test3 successfully hired.",result)

    def test_if_len_returns_correct(self):
        self.plantation.hire_worker("Test")
        self.plantation.planting("Test", "rose")
        self.assertEqual(1, len(self.plantation))
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test3", "rose")
        self.assertEqual(1, len(self.plantation))


    def test_planting_for_errors(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test", "rose")
        self.assertEqual("Worker with name Test is not hired!", str(ex.exception))

        self.plantation.hire_worker("Test")
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting("Test", "rose")
            self.plantation.planting("Test", "rose2")
            self.plantation.planting("Test", "rose3")
        self.assertEqual("The plantation is full!", str(ex.exception))
        self.assertEqual(2, len(self.plantation))

    def test_planting_with_correct_plantation(self):
        self.plantation.hire_worker("Test")
        result = self.plantation.planting("Test", "rose")
        self.assertEqual("Test planted it's first rose.",result)
        self.plantation.planting("Test", "rose2")
        self.assertEqual(self.plantation.plants, {"Test": ["rose", "rose2"]})
        self.assertEqual(len(self.plantation.plants["Test"]), 2)

    def test_if_str_returns_correct(self):
        self.plantation.hire_worker("Test")
        self.plantation.planting("Test", "rose")
        result = "Plantation size: 2\n"\
                 "Test\n"\
                 "Test planted: rose"
        self.assertEqual(result, self.plantation.__str__())

    def test_if_repr_returns_correct(self):

        self.plantation.hire_worker("Test")
        result = "Size: 2\n" \
                 "Workers: Test"
        self.assertEqual(result, self.plantation.__repr__())

if __name__ == '__main__':
    main()
