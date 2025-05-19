

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0  # Should return a boolean

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items[0]

    def rear(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)  # So it prints queue content properly

# Usage example
queue = Queue()
queue.enqueue(5)
queue.enqueue(1)
queue.enqueue(100)
queue.enqueue(10)

print(f"Queue content = {queue}")
print(f"Popped item = {queue.dequeue()}")
print(f"Front item = {queue.front()}")
print(f"Rear item = {queue.rear()}")
print(f"Size of queue = {queue.size()}")




