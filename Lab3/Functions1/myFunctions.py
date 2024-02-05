# my_functions.py

import math
import random


def sphere_volume(radius):
    volume = (4 / 3) * math.pi * (radius**3)
    return volume


def unique_elements(input_list):
    unique_list = []
    for element in input_list:
        if element not in unique_list:
            unique_list.append(element)
    return unique_list


def is_palindrome(word):
    cleaned_word = "".join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]


def histogram(numbers):
    for num in numbers:
        print("*" * num)


def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    secret_number = random.randint(1, 20)
    guesses_taken = 0

    while True:
        print("Take a guess.")
        guess = int(input())
        guesses_taken += 1

        if guess < secret_number:
            print("Your guess is too low.")
        elif guess > secret_number:
            print("Your guess is too high.")
        else:
            print(
                f"Good job, {name}! You guessed my number in {guesses_taken} {'guess' if guesses_taken == 1 else 'guesses'}!"
            )
            break
