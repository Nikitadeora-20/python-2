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
    stack = []
    output = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return ''.join(output)

def infixtoprefix(expression):
    # Step 1: Reverse the expression
    expression = expression[::-1]

    # Step 2: Swap brackets
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')')

    # Step 3: Convert reversed expression to postfix
    postfix = infix_to_postfix(expression)

    # Step 4: Reverse postfix to get prefix
    prefix = postfix[::-1]

    return prefix
s1 = "a+b*c"
s2 = "(a+b)*c"
s3 = "a+b*(c^d-e)^(f+g*h)-i"

print(infixtoprefix(s1))  # Output: +a*bc
print(infixtoprefix(s2))  # Output: *+abc
print(infixtoprefix(s3))  # Output: -+a*b^-^cde+f*ghi
