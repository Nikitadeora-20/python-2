class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Create nodes
drinks = Node("drinks")
hot = Node("hot")
cold = Node("cold")
tea = Node("tea")
coffee = Node("coffee")
cola = Node("cola")
fanta = Node("fanta")

# Build the tree
drinks.left = hot
drinks.right = cold

hot.left = tea
hot.right = coffee

cold.left = cola
cold.right = fanta

# Preorder traversal function
def inorder(node):
    if node is None:
        return
  
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# Start traversal
inorder(drinks)
