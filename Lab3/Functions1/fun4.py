def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def filter_prime(numbers):
    return list(filter(is_prime, numbers))


# Example usage:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

prime_numbers = filter_prime(numbers_list)

print("Prime numbers:", prime_numbers)
