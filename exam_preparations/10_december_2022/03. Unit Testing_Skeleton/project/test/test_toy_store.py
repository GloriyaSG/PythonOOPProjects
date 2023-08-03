from project.toy_store import ToyStore

from unittest import TestCase, main

class TestToyStore(TestCase):

    def setUp(self) -> None:
        self.toystore = ToyStore()

    def test_initalization(self):

        expected_shelves = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }

        self.assertEqual(expected_shelves, self.toystore.toy_shelf)

    def test_adding_toy_method_is_correct(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("W", "Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        self.toystore.add_toy("A", "Bear")
        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("A", "Bear")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.toystore.add_toy("A", "Mouse")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

        res = self.toystore.add_toy("B", "Mouse")
        self.assertEqual("Toy:Mouse placed successfully!", res)

    def test_if_remove_toy_is_correct(self):
        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("W", "Bear")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

        with self.assertRaises(Exception) as ex:
            self.toystore.remove_toy("A", "Bear")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

        self.toystore.add_toy("B", "Mouse")
        res = self.toystore.remove_toy("B", "Mouse")
        self.assertEqual("Remove toy:Mouse successfully!", res)
        self.assertEqual(self.toystore.toy_shelf["B"], None)


if __name__ == '__main__':
    main()

