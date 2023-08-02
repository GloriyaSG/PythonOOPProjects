from project.tennis_player import TennisPlayer

from unittest import TestCase, main

class TestTennisPlayer(TestCase):

    def setUp(self):
        self.player = TennisPlayer("Test", 25, 90)

    def test_initialization(self):
        self.assertEqual(self.player.name, "Test")
        self.assertEqual(self.player.age, 25)
        self.assertEqual(self.player.points, 90)
        self.assertEqual(self.player.wins, [])

    def test_if_name_setter_is_correct(self):
        self.player.name = "Test2"
        self.assertEqual(self.player.name, "Test2")

        with self.assertRaises(ValueError) as ex:
            self.player.name = "Te"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_if_age_setter_is_correct(self):
        self.player.age = 20
        self.assertEqual(self.player.age, 20)

        with self.assertRaises(ValueError) as ex:
            self.player.age = 7
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win(self):
        self.player.add_new_win("Australia Open")
        self.assertEqual(self.player.wins, ["Australia Open"])

        result = self.player.add_new_win("Australia Open")
        self.assertEqual("Australia Open has been already added to the list of wins!", result)

        self.player.add_new_win("Sofia Open")
        self.assertEqual(self.player.wins, ["Australia Open", "Sofia Open"])

    def test_lt_method(self):
        other = TennisPlayer("Test2", 20, 60)
        result = TennisPlayer.__lt__(self.player, other)
        self.assertEqual("Test is a better player than Test2", result)

        other = TennisPlayer("Test2", 20, 100)
        result = TennisPlayer.__lt__(self.player, other)
        self.assertEqual("Test2 is a top seeded player and he/she is better than Test", result)

    def test_str_method(self):
        self.player.add_new_win("Australia Open")
        self.player.add_new_win("Sofia Open")
        result = "Tennis Player: Test\n" \
                 "Age: 25\n" \
                 "Points: 90.0\n" \
                 "Tournaments won: Australia Open, Sofia Open"

        self.assertEqual(str(self.player), result)


if __name__ == '__main__':
    main()