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

    def evenodd(self):
        if self.head is None or self.head.next is None:
            return

        odd = self.head
        even = self.head.next
        even_head = even  # Store start of even list

        # Rearranging nodes
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head  # Append even list at end of odd list

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
ll.insert(3, 1)
ll.insert(10, 2)
ll.insert(7, 1)  # List: 5 -> 20 -> 10 -> 15

print("Before rearranging:")
ll.traversal()

ll.evenodd()

print("After rearranging odd/even positions:")
ll.traversal()
