# main.py

from myFunctions import (
    sphere_volume,
    unique_elements,
    is_palindrome,
    histogram,
    guess_the_number,
)

# Example usage of functions
print("Sphere Volume:", sphere_volume(5))

original_list = [1, 2, 2, 3, 4, 4, 5]
print("Original list:", original_list)
print("List with unique elements:", unique_elements(original_list))

input_word = "A man, a plan, a canal, Panama"
print(f'"{input_word}" is a palindrome: {is_palindrome(input_word)}')

print("Histogram:")
histogram([4, 9, 7])
