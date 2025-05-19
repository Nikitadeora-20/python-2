class stackqueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self,x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st1.append(self.st2.pop())


    def pop(self):
        if not self.st1:
            print("empty stack")
            return -1
        top_element=self.st1.pop()
        return top_element

    def peek(self):
        if not self.st1:
            print("empty stack")
            return -1
        return self.st1[-1]

    def isempty(self):
        return not self.st1

    def __str__(self):
        return str(self.st1)    

queue = stackqueue()
queue.push(10)
queue.push(20)
queue.push(30)
print(f"Queue after pushes: {queue}")
print(f"Popped element: {queue.pop()}")
print(f"Front element: {queue.peek()}")
print(f"Is empty? {queue.isempty()}")

