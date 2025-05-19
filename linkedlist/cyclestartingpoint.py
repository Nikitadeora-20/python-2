class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def create_cycle(self, pos):
        """Creates a cycle by connecting the last node to the node at position `pos` (0-based)."""
        if self.head is None:
            return

        tail = self.head
        cycle_node = None
        count = 0

        while tail.next is not None:
            if count == pos:
                cycle_node = tail
            tail = tail.next
            count += 1

        if cycle_node:
            tail.next = cycle_node

    def has_cycle(self):
        """Floyd's Cycle Detection Algorithm"""
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow=self.head
                while slow != fast :
                    slow = slow.next
                    fast = fast.next 

                return slow # Cycle detected

        return None  # No cycle

# Usage
ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)
ll.insert_end(5)

# Create a cycle: tail connects to node at position 2 (value = 3)
ll.create_cycle(2)

cycle_start = ll.has_cycle()
if cycle_start:
    print(f"Cycle detected. Starting node value: {cycle_start.val}")
else:
    print("No cycle in the linked list.")
