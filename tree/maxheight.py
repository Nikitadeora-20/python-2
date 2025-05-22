#recursive solution
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

# Recursive function to calculate the height of the tree
def solve(node):
    if node is None:
        return 0
    left_height = solve(node.left)
    right_height = solve(node.right)
    return 1 + max(left_height, right_height)

# Calling the function with the root node
print(solve(n1))

#iterative solution (level order)
from collections import deque

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

def level(root):
    if root is None:
        return 0
    queue = deque([root])
    height = 0
    while queue:
        level_size = len(queue)
        height += 1
        for _ in range(level_size):
            e = queue.popleft()
            if e.left:
                queue.append(e.left)
            if e.right:
                queue.append(e.right)
    return height

# Calling the function with the root node
l = level(n1)
print(l)

