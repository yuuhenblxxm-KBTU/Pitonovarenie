from movie_list import movies
from fun2_3 import movies_in_category
from fun2_4 import average_imdb


def average_imdb_by_category(category, movie_list):
    category_movies = movies_in_category(category, movie_list)
    return average_imdb(category_movies)


# Example usage:
avg_imdb_romance = average_imdb_by_category("Romance", movies)
print(avg_imdb_romance)
