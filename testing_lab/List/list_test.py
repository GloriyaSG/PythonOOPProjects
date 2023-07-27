from unittest import TestCase, main

from testing_lab.List.extended_list import IntegerList


class TestIntegerList(TestCase):
    def setUp(self):
        self.num_list = IntegerList(1,3,5,7.7)

    def test_init(self):
        res = self.num_list.get_data()
        expected = [1,3,5]
        self.assertEqual(expected, res)

    def test_add_invalid_value(self):
        with self.assertRaises(ValueError) as ex:
            self.num_list.add(6.5)

        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_valid_value(self):
        self.num_list.add(6)
        res = self.num_list.get_data()
        expected = [1,3,5,6]
        self.assertEqual(expected, res)

    def test_removing_invalid_index(self):
        with self.assertRaises(IndexError) as ex:
            self.num_list.remove_index(6)
        self.assertEqual("Index is out of range", str(ex.exception))


    def test_remove_valid_value(self):
        self.num_list.remove_index(2)
        res = self.num_list.get_data()
        expected = [1,3]
        self.assertEqual(expected, res)

    def test_getting_invalid_el_by_idx(self):
        with self.assertRaises(IndexError) as ex:
            self.num_list.get(6)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_getting_element_by_idx(self):
        res = self.num_list.get(0)
        expected = 1
        self.assertEqual(expected, res)

    def test_insert_invalid_idx_el(self):
        with self.assertRaises(IndexError) as ex:
            self.num_list.insert(6, 10)
        self.assertEqual("Index is out of range", str(ex.exception))


    def test_insert_non_int_element(self):
        with self.assertRaises(ValueError) as ex:
            self.num_list.insert(0, 6.5)
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_valid_idx_el(self):
        self.num_list.insert(1, 10)
        res = self.num_list.get_data()
        expected = [1,10,3,5]
        self.assertEqual(expected, res)

    def test_get_biggest(self):
        res = self.num_list.get_biggest()
        expected = 5
        self.assertEqual(expected, res)

    def test_get_idx(self):
        res = self.num_list.get_index(3)
        expected = 1
        self.assertEqual(expected, res)

if __name__ == '__main__':
    main()