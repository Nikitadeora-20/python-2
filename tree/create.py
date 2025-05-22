class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

drinks=Node("drinks")
hot=Node("hot")        
cold=Node("cold")
tea=Node("tea")
coffee=Node("coffee")
cola=Node("cola")
fanta=Node("fanta")

drinks.left=hot
drinks.right=cold

hot.left=tea
hot.right=coffee

cold.left=cola
cold.right=fanta



print(drinks)
print(drinks.val)
print(drinks.left.val)
print(drinks.right.val)