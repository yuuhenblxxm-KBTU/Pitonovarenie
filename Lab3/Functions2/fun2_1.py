from movie_list import movies


def above_threshold(movie):
    return movie["imdb"] > 5.5


# Example usage:
movie = {"name": "Usual Suspects", "imdb": 7.0, "category": "Thriller"}
print(above_threshold(movie))  # Output: True
