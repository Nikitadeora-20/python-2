def find_single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage:
nums = [2, 3, 5, 4, 5, 3, 4]
print(find_single_number(nums))  # Output: 2
