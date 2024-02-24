# Define the Node Class

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Define the Binary Tree Class
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    #  Implement Insertion Method
    def insert(self, data):
        # Check if the tree is empty
        if self.root is None:
            # create a new node as the root
            self.root = Node(data)
        else:
            # recursively insert the data
            self._insert(self.root, data)

