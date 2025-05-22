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

def diameter_of_binary_tree(root):
    diameter = 0

    def height(node):
        nonlocal diameter
        if node is None:
            return 0
        left_height = height(node.left)
        right_height = height(node.right)
        # Update the diameter if the path through root is larger
        diameter = max(diameter, left_height + right_height)
        # Return the height of the tree
        return 1 + max(left_height, right_height)

    height(root)
    return diameter

# Calling the function with the root node
print(diameter_of_binary_tree(n1))
