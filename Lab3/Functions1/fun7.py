def has_double_threes(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False


numbers = [1, 2, 3, 3, 4, 5]
result = has_double_threes(numbers)
print(result)
