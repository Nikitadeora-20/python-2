class Node:
    def __init__(self, val):
        self.val = val  # Ensure val is an integer
        self.left = None
        self.right = None

# Constructing the binary tree
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

def maximumpathsum(root):
    max_i = float('-inf')  # Proper initialization

    def check_height(node):
        nonlocal max_i  # To modify the outer variable
        if node is None:
            return 0
        left_sum = max(check_height(node.left), 0)
        right_sum = max(check_height(node.right), 0)
        max_i = max(max_i, left_sum + node.val + right_sum)
        return node.val + max(left_sum, right_sum)

    check_height(root)
    return max_i

# Calling the function with the root node
print(maximumpathsum(n1))

