def remove_last_set_bit(n):
    return n & (n - 1)

# Example usage:
number = 12  # binary: 1100
print("Original:", bin(number))
new_number = remove_last_set_bit(number)
print("After removing last set bit:", bin(new_number))
