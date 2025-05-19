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

    def delete(self, val):
        temp = self.head

        # Empty list
        if temp is None:
            print("List is empty")
            return

        # If head node is the one to delete
        if temp.val == val:
            self.head = temp.next
            return

        # Traverse to find the node
        prev = None
        found = False
        while temp is not None:
            if temp.val == val:
                found = True
                break
            prev = temp
            temp = temp.next

        if found:
            prev.next = temp.next
        else:
            print("Value not found")

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
ll.insert(5,0)
ll.insert(20,1)
ll.insert(25,2)

ll.delete(20)  # Will print "List is empty"
ll.traversal()  # Will print "SLL is empty"
