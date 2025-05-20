class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, val):
        if len(self.items) == 0:
            self.items.append([val, val])
        else:
            mini = min(self.items[-1][1], val)
            self.items.append([val, mini])

    def getmin(self):
        if len(self.items) == 0:
            return "stack is empty"
        return self.items[-1][1]

    def pop(self):
        if len(self.items) == 0:
            return "cannot pop, stack is empty"
        x = self.items.pop()
        return x[0]

    def top(self):
        if len(self.items) == 0:
            return "cannot top, stack is empty"
        return self.items[-1][0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str([item[0] for item in self.items])  # Show only the values


# ✅ Test the stack
stack = Stack()
stack.push(5)
stack.push(3)
stack.push(10)

print(f"stack content = {stack}")
print(f"popped item = {stack.pop()}")
print(f"top item = {stack.top()}")
print(f"size of stack = {stack.size()}")
print(f"stack content = {stack}")
print(f"minimum element = {stack.getmin()}")
print(f"popped item = {stack.pop()}")
print(f"top item = {stack.top()}")
print(f"minimum element = {stack.getmin()}")
print(f"size of stack = {stack.size()}")
