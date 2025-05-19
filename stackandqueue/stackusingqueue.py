#in these we use dequeue it means double ended queue
#it allow both operation from both side that is insertion and deletion 
#it work like adoubly linked list 

from collections import deque
class Stack:
    def __init__(self):
        self.queue=deque()

    def push(self,item):
        self.queue.append(item)
        for _ in range(len(self.queue)-1):
            self.queue.append(self.queue.popleft()) 

    def pop(self):
        if len(self.queue)==0:
            return "stack is empty"
        return self.queue.popleft()

    def peek(self):
        if len(self.queue)==0:
            return "stack is empty"
        return self.queue[0]

    def isempty(self):
        return len(self.queue)==0

    def size(self):
        return len(self.queue)==0

    def __str__(self):
        return str(self.queue)

queue =Stack()
queue.push(5)
queue.push(10)
queue.push(15)
queue.push(20)
print(f" {queue}")
print(f"stack content ={queue}")
print(f"popped items = {queue.pop()}")
print(f"top item={queue.peek()}")
print(f"size of stack = {queue.size()}")                            