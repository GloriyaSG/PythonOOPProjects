from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self):
        self.mammal = Mammal("Mickey", "mouse", "Okay")

    def test_if_make_sound_returns_correct_value(self):
        self.assertEqual("Mickey makes Okay", self.mammal.make_sound())

    def test_if_get_kingdom_returns_correct_value(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_if_info_returns_correct_value(self):
        self.assertEqual("Mickey is of type mouse", self.mammal.info())

if __name__ == '__main__':
    main()