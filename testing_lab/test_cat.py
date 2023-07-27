
class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0


    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1


    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


from unittest import TestCase, main


class CatTest(TestCase):

    def setUp(self):
        self.cat = Cat('John')

    def test_initializing(self):
        self.assertEqual("John",self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_if_size_is_increased_after_eating(self):
        self.cat.eat()
        self.assertEqual(1, self.cat.size)
        self.assertEqual(True, self.cat.sleepy)
        self.assertEqual(True, self.cat.fed)

    def test_if__cat_cannot_eat_if_already_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_if_cat_can_sleep_if_hungry(self):
        self.cat.fed = False
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_if_cat_can_sleep_after_sleeping(self):
        self.cat.sleepy = True
        self.cat.fed = True
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)

if __name__ == '__main__':
    main()