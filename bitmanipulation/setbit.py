def set_ith_bit(n, i):
    return n | (1 << i)

# Example
number = 9      # Binary: 1001
i = 1           # We want to set the 1st bit

result = set_ith_bit(number, i)
print(f"Original: {bin(number)} ({number})")
print(f"After setting {i}-th bit: {bin(result)} ({result})")
