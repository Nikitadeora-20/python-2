#simple linked list 
# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Stack class using linked list
class Stack:
    def __init__(self):
        self.top = None  # Initially the stack is empty

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top  # Point new node to the old top
        self.top = new_node       # Update top to the new node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_node = self.top
        self.top = self.top.next  # Move top to the next node
        return popped_node.data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Stack (top -> bottom):", elements)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

stack.display()        # Stack (top -> bottom): [30, 20, 10]
print("Top:", stack.peek())  # Top: 30

print("Popped:", stack.pop())  # Popped: 30
stack.display()                # Stack (top -> bottom): [20, 10]


#using doubly linked list
# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Stack class using Doubly Linked List
class Stack:
    def __init__(self):
        self.top = None  # Top of stack

    def push(self, data):
        new_node = Node(data)
        if self.top is not None:
            self.top.next = new_node
            new_node.prev = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        popped_data = self.top.data
        self.top = self.top.prev
        if self.top:
            self.top.next = None
        return popped_data

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def display(self):
        current = self.top
        elements = []
        while current:
            elements.append(current.data)
            current = current.prev
        print("Stack (top -> bottom):", elements)
stack = Stack()
stack.push(100)
stack.push(200)
stack.push(300)

stack.display()             # Stack (top -> bottom): [300, 200, 100]
print("Top:", stack.peek())  # Top: 300

print("Popped:", stack.pop())  # Popped: 300
stack.display()                # Stack (top -> bottom): [200, 100]
