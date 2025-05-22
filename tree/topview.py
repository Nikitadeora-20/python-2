from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def top_view(root):
    if not root:
        return []

    # Dictionary to store the first node at each horizontal distance
    hd_node = {}
    # Queue for BFS: stores pairs of node and its horizontal distance
    queue = deque([(root, 0)])

    while queue:
        node, hd = queue.popleft()

        # If horizontal distance is not present in the dictionary, add it
        if hd not in hd_node:
            hd_node[hd] = node.val

        # Enqueue left and right children with updated horizontal distances
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))

    # Extract the values in order of horizontal distances
    top_view_nodes = [hd_node[hd] for hd in sorted(hd_node)]
    return top_view_nodes

# Example usage:
if __name__ == "__main__":
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

    result = top_view(n1)
    print("Top view of the binary tree:", result)
