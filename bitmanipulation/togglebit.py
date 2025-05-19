def toggle_ith_bit(n, i):
    return n ^ (1 << i)

# Example usage:
number = 13  # binary: 1101
i = 2

new_number = toggle_ith_bit(number, i)
print("Original number:", number, "-> Binary:", bin(number))
print(f"After toggling bit {i}:", new_number, "-> Binary:", bin(new_number))
