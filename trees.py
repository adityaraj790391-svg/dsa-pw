class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

root = Node(5)
root.left =  Node(3)
root.right = Node(9)
root.left.right = Node(1)
root.left.left = Node(0)

print(root.left.data)

        