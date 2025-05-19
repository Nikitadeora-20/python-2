def clear_ith_bit(n, i):
    return n & ~(1 << i)

# Example usage:
number = 13  # binary: 1101
i = 2

new_number = clear_ith_bit(number, i)
print("Original number:", number, "-> Binary:", bin(number))
print(f"After clearing bit {i}:", new_number, "-> Binary:", bin(new_number))
