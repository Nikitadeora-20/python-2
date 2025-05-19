class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)        

    def pop(self):
        if len(self.items)==0:
            return"cannot pop, stack is empty"
        x=self.items.pop()
        return x 

    def top(self):
        if len(self.items)==0:
            return"cannot top,stack is empty"
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)  # So it prints queue content properly
    

stack =Stack()
stack.push(5)
stack.push(3)
stack.push(10)
print(f"stack content ={stack}")
print(f"popped items = {stack.pop()}")
print(f"top item={stack.top()}")
print(f"size of stack = {stack.size()}")                            