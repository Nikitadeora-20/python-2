def is_operator(c):
    return c in "+-*/^"

def prefix_to_postfix(expression):
    stack = []

    # Traverse the expression from right to left
    for char in reversed(expression):
        if char.isalnum():#in python isalnum used for a-z , A-Z , 0-9 operand 
            stack.append(char)
        elif is_operator(char):
            if len(stack) < 2:
                return "Error: Invalid prefix expression"
            op1 = stack.pop()
            op2 = stack.pop()
            new_expr = op1 + op2 + char
            stack.append(new_expr)
        else:
            return f"Error: Invalid character '{char}' in expression"

    if len(stack) != 1:
        return "Error: Invalid prefix expression"

    return stack[0]
expr1 = "+a*bc"        # a + (b * c)
expr2 = "*+abc"        # (a + b) * c
expr3 = "-+a*b^-^cde+f*ghi" # full complex expression
expr4= "*+pq-mn"
print(prefix_to_postfix(expr1))  # abc*+
print(prefix_to_postfix(expr2))  # ab+c*
print(prefix_to_postfix(expr3))  # abcd^e-fgh*+^*+i-
print(prefix_to_postfix(expr4))