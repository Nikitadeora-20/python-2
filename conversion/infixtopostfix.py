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

def infix_to_postfix(expression):
    stack = []  # operator stack
    output = []  # result list

    for char in expression:
        if char.isalnum():  # operand (variable or number)
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # remove '(' from stack
        elif is_operator(char):
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)

    # Pop remaining operators
    while stack:
        output.append(stack.pop())

    return ''.join(output)
expr1 = "a+b*c"
expr2 = "(a+b)*c"
expr3 = "a+b*(c^d-e)^(f+g*h)-i"

print(infix_to_postfix(expr1))  # abc*+
print(infix_to_postfix(expr2))  # ab+c*
print(infix_to_postfix(expr3))  # abcd^e-fgh*+^*+i-
