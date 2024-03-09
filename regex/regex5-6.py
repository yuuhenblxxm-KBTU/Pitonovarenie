import re

def func(text):
    pattern = r'[ ,.]'
    replaced_text = re.sub(pattern, ':', text)
    return replaced_text

input_text = input("Enter a string: ")
result = func(input_text)
print("Result:", result)
def sum_and_product(list1, list2):
    sum_result = sum(list1) + sum(list2)
    product_result = 1
    for num in list1 + list2:
        product_result *= num
    return sum_result, product_result

# Example usage:
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

sum_result, product_result = sum_and_product(list1, list2)
print("Sum:", sum_result)
print("Product:", product_result)
