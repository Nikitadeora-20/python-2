def is_power_of_two(n):
    return n > 0 and (n & (n - 1)) == 0

# Example usage:
num = 16
print(is_power_of_two(num))  # True

num = 18
print(is_power_of_two(num))  # False
