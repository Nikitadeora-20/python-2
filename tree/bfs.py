from collections import deque
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

def level(node):
    result=[]
    queue=deque([])
    queue.append(node)
    while len(queue)!=0:
        e=queue.popleft()
        result.append(e.val)
        if e.left is not None:
            queue.append(e.left)
        if e.right is not None:
            queue.append(e.right)
    return result  
p1=level(drinks)
print(p1)                 