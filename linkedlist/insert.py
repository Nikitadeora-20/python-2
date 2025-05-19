class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val, position):
        new_node = Node(val)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            prev_node = None
            count = 0
            while current is not None and count < position:
                prev_node = current
                current = current.next
                count += 1
            if prev_node is None:
                print("Invalid position")
                return
            prev_node.next = new_node
            new_node.next = current

    def traversal(self):
        if self.head is None:
            print("SLL is empty")
        else:
            current = self.head
            while current is not None:
                print(current.val, end=" -> ")
                current = current.next
            print("None")

# Usage
ll = LinkedList()

# Manually adding initial nodes
ll.insert(5, 0)
ll.insert(10, 1)
ll.insert(15, 2)

# Insert 20 at position 1
ll.insert(20, 1)

# Print the linked list
ll.traversal()
             