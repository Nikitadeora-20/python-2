def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    return c in "+-*/^"

def is_operator(c):
    return c in "+-*/^"

def prefix_to_infix(expression):
    stack = []

    for char in expression[::-1]:
        if char.isalnum():
            stack.append(char)
        elif is_operator(char):
            if len(stack) < 2:
                return "Error: Invalid postfix expression"
            operand1 = stack.pop()
            operand2 = stack.pop()
            new_expr = f"({operand1}{char}{operand2})"
            stack.append(new_expr)
        else:
            return f"Error: Invalid character '{char}' in expression"

    if len(stack) != 1:
        return "Error: Invalid postfix expression"

    return stack[0]
expr1 = "+a*bc"
expr2 = "*+abc"
expr3 = "-+a*b^-^cde+f*ghi"

print(prefix_to_infix(expr1))  # (a+(b*c))
print(prefix_to_infix(expr2))  # ((a+b)*c)
print(prefix_to_infix(expr3))  # ((a+((b*((((c^d)-e)^((f+(g*h)))))))-i))


