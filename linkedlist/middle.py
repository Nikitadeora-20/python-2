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

    def middle(self):
        n = 0
        temp = self.head
        while temp is not None:
            temp = temp.next
            n += 1

        temp = self.head
        for i in range(0, n // 2):
            temp = temp.next
        return temp

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
ll.insert(5, 0)
ll.insert(10, 1)
ll.insert(15, 2)
ll.insert(20, 3)
ll.insert(25, 4)

# Print traversal
ll.traversal()

# Get and print middle node
mid_node = ll.middle()
if mid_node:
    print(f"Middle node value: {mid_node.val}")
else:
    print("List is empty")
