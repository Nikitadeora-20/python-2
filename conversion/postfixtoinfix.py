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

def postfix_to_infix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        elif is_operator(char):
            if len(stack) < 2:
                return "Error: Invalid postfix expression"
            operand2 = stack.pop()
            operand1 = stack.pop()
            new_expr = f"({operand1}{char}{operand2})"
            stack.append(new_expr)
        else:
            return f"Error: Invalid character '{char}' in expression"

    if len(stack) != 1:
        return "Error: Invalid postfix expression"

    return stack[0]
expr1 = "abc*+"       # a + b * c
expr2 = "ab+c*"       # (a + b) * c
expr3 = "abcd^e-fgh*+^*+i-"  # a + b * (c ^ d - e) ^ (f + g * h) - i

print(postfix_to_infix(expr1))  # (a+(b*c))
print(postfix_to_infix(expr2))  # ((a+b)*c)
print(postfix_to_infix(expr3))  # ((a+((b*((((c^d)-e)^((f+(g*h)))))))-i))
