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


'''
Types of Binary Tree
• Full Binary Tree - A full Binary tree is a special type of binary tree in which every parent node/internal node has either two or no children.
• Perfect Binary Tree - A perfect binary tree is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes tare at the same level.
• Complete Binary Tree - A complete binary tree is just like a full binary tree, but with two major differences
Every level must be completely filled, All the leaf elements must lean towards the left. The last leaf element might not have a right sibling i.e. a complete binary tree doesn't have to be a full binary tree.
• Degenerate / Skewed Binary Tree - all nodes go only in one direction, like a straight line.
It looks more like a linked list than a normal tree.
• Balanced Binary Tree - It is a type of binary tree in which the difference between the height of the left and the right subtree for each node is either 0 or 1.
'''

'''
Types of Traversal - 
Pre Order Traversal
Post Order Traversal
In Order Traversal
Level Order Traversal
'''

        