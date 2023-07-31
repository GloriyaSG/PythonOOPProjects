from project.movie import Movie

from unittest import TestCase, main

class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie("Game of Thrones", 2016, 9.6)

    def test_initilization(self):
        self.assertEqual("Game of Thrones", self.movie.name)
        self.assertEqual(2016, self.movie.year)
        self.assertEqual(9.6, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter_for_invalid_name(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ""
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_for_invalid_year(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1800
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_for_adding_actors(self):
        self.movie.add_actor("Test")
        self.assertEqual(1, len(self.movie.actors))

        result = self.movie.add_actor("Test")
        self.assertEqual("Test is already added in the list of actors!", result)

    def test_gt_if_returns_correct(self):
        self.movie.rating = 10
        other = Movie("Test2", 2017, 6.6)
        result = Movie.__gt__(self.movie, other)
        self.assertEqual('"Game of Thrones" is better than "Test2"', result)

        self.movie.rating = 5.6
        result = Movie.__gt__(self.movie, other)
        self.assertEqual('"Test2" is better than "Game of Thrones"', result)

    def test_if_repr_is_correct(self):
        self.movie.add_actor("Test2")
        result = "Name: Game of Thrones\n" \
                 "Year of Release: 2016\n" \
                 "Rating: 9.60\n" \
                 "Cast: Test2"
        self.assertEqual(result, repr(self.movie))

if __name__ == '__main__':
    main()

