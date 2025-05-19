class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_end(self, val):
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def remove_nth_from_end(self, n):
        dummy = Node(0)
        dummy.next = self.head
        fast = dummy
        slow = dummy

        # Move fast ahead by n steps
        for _ in range(n):
            if fast.next is None:
                print("n is greater than the length of the list.")
                return
            fast = fast.next

        # Move both pointers until fast reaches the end
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete the nth node from end
        slow.next = slow.next.next

        # Update head (in case the removed node was the first)
        self.head = dummy.next

    def traversal(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.insert_end(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_end(40)
ll.insert_end(50)

print("Original list:")
ll.traversal()

ll.remove_nth_from_end(2)  # Removes 2nd node from end (40)

print("After removing 2nd node from end:")
ll.traversal()
