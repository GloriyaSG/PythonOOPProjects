# Python OOP Retake Exam - 18 April 2022 - Movie App

# https://judge.softuni.org/Contests/Practice/Index/3431#1
=============================================================================================
# file name: movie.py

from abc import ABC, abstractmethod


class Movie(ABC):
    def __init__(self, title: str, year: int, owner: object, age_restriction: int):
        self.title = title
        self.year = year
        self.owner = owner
        self.age_restriction = age_restriction
        self.likes = 0

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('The title cannot be empty string!')
        self.__title = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value < 1888:
            raise ValueError("Movies weren't made before 1888!")
        self.__year = value

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if not type(value).__name__ == 'User':
            raise ValueError('The owner must be an object of type User!')
        self.__owner = value

    @abstractmethod
    def details(self):
        ...


=============================================================================================
# file name: action.py

from project.movie_specification.movie import Movie


class Action(Movie):
    def __init__(self, title: str, year: int, owner: object, age_restriction=12):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 12:
            raise ValueError("Action movies must be restricted for audience under 12 years!")
        self.__age_restriction = value

    def details(self):
        return f"Action - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"


=============================================================================================
# file name: fantasy.py

from project.movie_specification.movie import Movie


class Fantasy(Movie):
    def __init__(self, title, year, owner, age_restriction=6):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 6:
            raise ValueError("Fantasy movies must be restricted for audience under 6 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

=============================================================================================
# file name: thriller.py

from project.movie_specification.movie import Movie


class Thriller(Movie):
    def __init__(self, title, year, owner, age_restriction=16):
        super().__init__(title, year, owner, age_restriction)

    @property
    def age_restriction(self):
        return self.__age_restriction

    @age_restriction.setter
    def age_restriction(self, value):
        if value < 16:
            raise ValueError("Thriller movies must be restricted for audience under 16 years!")
        self.__age_restriction = value

    def details(self):
        return f"Fantasy - Title:{self.title}, Year:{self.year}, " \
               f"Age restriction:{self.age_restriction}, Likes:{self.likes}, Owned by:{self.owner.username}"

=============================================================================================
# file name: user.py

class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []  # Objs
        self.movies_owned = []  # Objs

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if len(value) == 0:
            raise ValueError('Invalid username!')
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError('Users under the age of 6 are not allowed!')
        self.__age = value

    def __str__(self):
        result_str = [f'Username: {self.username}, Age: {self.age}', 'Liked movies:']
        if len(self.movies_liked) > 0:
            for liked in self.movies_liked:
                result_str.append(liked.details())
        else:
            result_str.append('No movies liked.')
        result_str.append('Owned movies:')
        if len(self.movies_owned) > 0:
            for owned in self.movies_owned:
                result_str.append(owned.details())
        else:
            result_str.append('No movies owned.')
        return '\n'.join(result_str)

=============================================================================================
# file name: movie_app.py

from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def check_if_user_exists(self, username):
        for user in self.users_collection:
            if user.username == username:
                return True
        return False

    def check_if_movie_exists(self, title):
        for movie in self.movies_collection:
            if movie.title == title:
                return True
        return False

    def check_if_user_liked_movie(self, username, movie_title):
        for user in self.users_collection:
            if user.username == username:
                for movie in user.movies_liked:
                    if movie.title == movie_title:
                        return True
                return False

    def register_user(self, username, age):
        if self.check_if_user_exists(username):
            raise Exception('User already exists!')
        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f'{username} registered successfully.'

    def upload_movie(self, username, movie):
        if not self.check_if_user_exists(username):
            raise Exception('This user does not exist!')
        elif self.check_if_movie_exists(movie.title):
            raise Exception('Movie already added to the collection!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.append(movie)
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.append(movie)
                    return f'{username} successfully added {movie.title} movie.'

    def edit_movie(self, username, movie, **kwargs):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            for attr, new_value in kwargs.items():
                setattr(movie, attr, new_value)
            return f'{username} successfully edited {movie.title} movie.'

    def delete_movie(self, username, movie):
        if not self.check_if_movie_exists(movie.title):
            raise Exception(f'The movie {movie.title} is not uploaded!')
        elif not username == movie.owner.username:
            raise Exception(f'{username} is not the owner of the movie {movie.title}!')
        else:
            self.movies_collection.pop(self.movies_collection.index(movie))
            for user in self.users_collection:
                if user.username == username:
                    user.movies_owned.pop(user.movies_owned.index(movie))
                    return f'{username} successfully deleted {movie.title} movie.'

    def like_movie(self, username, movie):
        if username == movie.owner.username:
            raise Exception(f'{username} is the owner of the movie {movie.title}!')
        elif self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} already liked the movie {movie.title}!')
        else:
            movie.likes += 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.append(movie)
            return f'{username} liked {movie.title} movie.'

    def dislike_movie(self, username, movie):
        if not self.check_if_user_liked_movie(username, movie.title):
            raise Exception(f'{username} has not liked the movie {movie.title}!')
        else:
            movie.likes -= 1
            for user in self.users_collection:
                if user.username == username:
                    user.movies_liked.pop(user.movies_liked.index(movie))
            return f'{username} disliked {movie.title} movie.'

    def display_movies(self):
        if len(self.movies_collection) == 0:
            return 'No movies found.'
        else:
            result_str = []
            for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)):
                result_str.append(movie.details())
            return '\n'.join(result_str)

    def __str__(self):
        if len(self.users_collection) == 0:
            users = 'No users.'
        else:
            users = ', '.join([user.username for user in self.users_collection])
        if len(self.movies_collection) == 0:
            movies = 'No movies.'
        else:
            movies = ', '.join([movie.title for movie in self.movies_collection])

        return f'All users: {users}\nAll movies: {movies}'

