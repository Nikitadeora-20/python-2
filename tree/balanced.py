class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Constructing the binary tree
n1 = Node("1")
n2 = Node("2")
n3 = Node("3")
n4 = Node("4")
n5 = Node("5")
n6 = Node("6")
n7 = Node("7")

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

# Recursive function to check if the tree is balanced
def is_balanced(node):
    def check_height(n):
        if n is None:
            return 0
        left_height = check_height(n.left)
        if left_height == -1:
            return -1
        right_height = check_height(n.right)
        if right_height == -1:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return 1 + max(left_height, right_height)
    
    return check_height(node) != -1

# Calling the function with the root node
print(is_balanced(n1))
