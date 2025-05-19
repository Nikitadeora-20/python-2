def count_bits_to_flip(a, b):
    xor = a ^ b
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

# Example usage:
a = 29   # binary 11101
b = 15   # binary 01111

print(count_bits_to_flip(a, b))  # Output: 2
