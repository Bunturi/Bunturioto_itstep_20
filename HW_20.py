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

    def _insert(self, data, current_node):
        # Compare the data to be inserted with the data of the current node
        if data < current_node.data:
            # If the data is less than the current node's data,
            # go to the left subtree
            if current_node.left is None:
                # If the left child is None, create a new node with the data
                # and set it as the left child of the current node
                current_node.left = Node(data)
            else:
                # If the left child is not None, recursively call _insert
                # with the left child as the new current node
                self._insert(data, current_node.left)

        elif data > current_node.data:
            # If the data is greater than the current node's data,
            # go to the right subtree
            if current_node.right is None:
                # If the right child is None, create a new node with the data
                # and set it as the right child of the current node
                current_node.right = Node(data)
            else:
                # If the right child is not None, recursively call _insert
                # with the right child as the new current node
                self._insert(data, current_node.right)
        else:
            # If the data is equal to the current node's data,
            # it's a duplicate value
            print("Value already in tree!")



