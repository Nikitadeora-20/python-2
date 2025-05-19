def print_subsequences(s, index=0, current=""):
    if index == len(s):
        print(current)
        return
    
    # Include current character
    print_subsequences(s, index + 1, current + s[index])
    
    # Exclude current character
    print_subsequences(s, index + 1, current)

# Example usage
s = "abc"
print_subsequences(s)
