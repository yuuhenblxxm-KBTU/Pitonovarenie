def is_palindrome(word):
    cleaned_word = "".join(char.lower() for char in word if char.isalnum())
    return cleaned_word == cleaned_word[::-1]


input_word = "A man, a plan, a canal, Panama"
result = is_palindrome(input_word)
print(result)
