from typing import List

from project.movie_specification.movie import Movie
from project.movie_specification.action import Action
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.thriller import Thriller
from project.user import User


class MovieApp:

    def __init__(self):

        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username:str, age:int):
        for user in self.users_collection:
            if user.username == username:
                raise Exception("User already exists!")
        user_curr = User(username,age)
        self.users_collection.append(user_curr)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = [us for us in self.users_collection if us.username == username]

        if not user:
            raise Exception(f"This user does not exist!")

        curr_user = user[0]
        if movie.owner.username != curr_user.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        if movie in self.movies_collection:
            raise Exception(f"Movie already added to the collection!")

        curr_user.movies_owned.append(movie)
        self.movies_collection.append(movie)

        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):

        key_values = {
            'title': movie.title,
            'year': movie.year,
            'age_restriction': movie.age_restriction
        }

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user_curr = [user for user in self.users_collection if user.username == username][0]
        if movie.owner.username != user_curr.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        for key, value in kwargs.items():
            key_values[key] = value

        movie.title = key_values['title']
        movie.year = key_values['year']
        movie.age_restriction = key_values['age_restriction']

        return f"{username} successfully edited {movie.title} movie."


    def delete_movie(self, username: str, movie: Movie):
        user_curr = [user for user in self.users_collection if user.username == username][0]

        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")

        if movie.owner.username != user_curr.username:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")

        self.movies_collection.remove(movie)
        user_curr.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self,username: str, movie: Movie):
        user_curr = [user for user in self.users_collection if user.username == username][0]

        if movie.owner.username == user_curr.username:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user_curr.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        user_curr.movies_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user_curr = [user for user in self.users_collection if user.username == username][0]

        if movie not in user_curr.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")

        user_curr.movies_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return f"No movies found."

        result = []
        sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))

        for movie in sorted_movies:
            result.append(movie.details())

        return '\n'.join(result)

    def __str__(self):
        result = []

        if not self.users_collection:
            result.append(f"All users: No users.")
        else:
            result.append(f"All users: {', '.join([user.username for user in self.users_collection])}")

        if not self.movies_collection:
            result.append(f"All movies: No movies.")
        else:
            result.append(f"All movies: {', '.join([movie.title for movie in self.movies_collection])}")

        return '\n'.join(result)

