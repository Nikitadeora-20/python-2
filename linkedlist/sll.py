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

# Function to print the linked list
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Print the linked list
print_list(node1)
