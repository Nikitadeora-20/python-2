#single linkedlist
# Node class for Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class using Linked List
class Queue:
    def __init__(self):
        self.front = None  # Points to the front of the queue
        self.rear = None   # Points to the rear of the queue

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
            return
        # Add new node at the end and change rear
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        # Remove front node
        removed_data = self.front.data
        self.front = self.front.next
        # If front becomes None, queue is empty, set rear to None too
        if self.front is None:
            self.rear = None
        return removed_data

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Queue (front -> rear):", elements)
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

queue.display()              # Queue (front -> rear): [10, 20, 30]
print("Front:", queue.peek())  # Front: 10

print("Dequeued:", queue.dequeue())  # Dequeued: 10
queue.display()                      # Queue (front -> rear): [20, 30]


#doubly linked list
# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Queue class using Doubly Linked List
class Queue:
    def __init__(self):
        self.front = None  # Points to the front node
        self.rear = None   # Points to the rear node

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            # Queue is empty
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            # Queue is now empty
            self.rear = None
        else:
            self.front.prev = None
        return removed_data

    def peek(self):
        if self.front is None:
            print("Queue is empty")
            return None
        return self.front.data

    def is_empty(self):
        return self.front is None

    def display(self):
        current = self.front
        elements = []
        while current:
            elements.append(current.data)
            current = current.next
        print("Queue (front -> rear):", elements)
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()               # Queue (front -> rear): [10, 20, 30]
print("Front:", q.peek())  # Front: 10

print("Dequeued:", q.dequeue())  # Dequeued: 10
q.display()                      # Queue (front -> rear): [20, 30]
