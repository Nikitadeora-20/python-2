def is_ith_bit_set(n, i):
    # Shift 1 to the left i times, then AND with n
    return (n & (1 << i)) != 0

# Example
number = 13  # Binary: 1101
i = 2

if is_ith_bit_set(number, i):
    print(f"The {i}-th bit is set.")
else:
    print(f"The {i}-th bit is not set.")
