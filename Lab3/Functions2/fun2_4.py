from movie_list import movies


def average_imdb(movie_list):
    return sum(movie["imdb"] for movie in movie_list) / len(movie_list)


# Example usage:
avg_imdb = average_imdb(movies)
print(avg_imdb)
