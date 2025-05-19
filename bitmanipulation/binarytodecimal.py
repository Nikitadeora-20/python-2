def binary_to_decimal(binary_str):
    decimal = 0
    power = 0

    # Start from the rightmost bit
    for digit in reversed(binary_str):
        if digit == '1':
            decimal += 2 ** power
        power += 1

    return decimal

# Test
binary = "1101"
result = binary_to_decimal(binary)
print(result)  # Output: 13



#second method
binary = "1101"
decimal = int(binary, 2)
print(decimal)  # Output: 13
