class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create nodes and link them
node1 = Node(5)
node2 = Node(10)
node3 = Node(15)

node1.next = node2
node2.next = node3

def traversal(head):
    if head is None:
        print("SLL is empty")
    else:
        current = head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None\nSLL is not empty")

# Call the function
traversal(node1)
