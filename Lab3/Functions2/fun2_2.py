# movies_above_threshold.py
from movie_list import movies
from fun2_1 import above_threshold


def movies_above_threshold(movie_list):
    return [movie for movie in movie_list if above_threshold(movie)]


# Example usage:
filtered_movies = movies_above_threshold(movies)
print(filtered_movies)
