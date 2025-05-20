def is_operator(c):
    return c in "+-*/^"

def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        elif is_operator(char):
            if len(stack) < 2:
                return "Error: Invalid postfix expression"
            op2 = stack.pop()
            op1 = stack.pop()
            new_expr = char + op1 + op2
            stack.append(new_expr)
        else:
            return f"Error: Invalid character '{char}' in expression"

    if len(stack) != 1:
        return "Error: Invalid postfix expression"

    return stack[0]
expr1 = "abc*+"        # a + b * c
expr2 = "ab+c*"        # (a + b) * c
expr3 = "abcd^e-fgh*+^*+i-"  # a + b * (c ^ d - e) ^ (f + g * h) - i

print(postfix_to_prefix(expr1))  # +a*bc
print(postfix_to_prefix(expr2))  # *+abc
print(postfix_to_prefix(expr3))  # -+a*b^-^cde+f*ghi
