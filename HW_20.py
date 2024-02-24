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

    def _insert(self, current_node, data):
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
                self._insert(current_node.left, data)

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
                self._insert(current_node.right, data)
        else:
            # If the data is equal to the current node's data,
            # it's a duplicate value
            print("Value already in tree!")

    # Method to print the parent tree starting from the root
    def printParent(self):
        print("Printing Parent Tree")
        self._printParent(self.root, None)

    # Helper method to recursively print the parent of each node
    def _printParent(self, node, parent):
        # If the current node is not None
        if node is not None:
            # If the parent is None, it means the current node is the root
            if parent is None:
                print(node.data, "-> root")
            else:
                print(node.data, "->", parent.data)
            # Recursively call _printParent on the left and right child of the current node,
            # passing the current node as the parent
            self._printParent(node.left, node)
            self._printParent(node.right, node)

    def print_tree(self, node, level=0, prefix='Root: '):
        # Check if the current node is not None
        if node is not None:
            # Print the current node's data with appropriate indentation based on the level
            print(' ' * (level * 4) + prefix + str(node.data))
            # Check if the current node has either a left child or a right child
            if node.left is not None or node.right is not None:
                self.print_tree(node.left, level + 1, prefix='L-- ')
                self.print_tree(node.right, level + 1, prefix='R-- ')

    # Define the count_edges method
    def count_edges(self):
        # Check if the tree is empty
        if self.root is None:
            return 0
        # Call the helper method to count edges starting from the root node
        return self._count_edges(self.root)

    # Helper method to recursively count the number
    # of edges in the binary tree
    def _count_edges(self, node):
        if node is None:
            return 0
        # Recursively count the number of edges in the left subtree,
        # the right subtree, and add 1 for the current edge
        return self._count_edges(node.left) + self._count_edges(node.right) + 1

    # Define the print_leaf_nodes method
    def print_leaf_nodes(self):
        print("Leaf Nodes:")
        self._print_leaf_nodes(self.root)

    def _print_leaf_nodes(self, node):
        # Check if the current node is not None
        if node is not None:
            # Check if the current node is a leaf node if it is:print
            if node.left is None and node.right is None:
                print(node.data, end=" ")
            # Recursively call _print_leaf_nodes on the
            # left and right child of the current node
            self._print_leaf_nodes(node.left)
            self._print_leaf_nodes(node.right)

    # Finding the Maximum Value in the Tree
    def find_max(self):
        if self.root is None:
            # If the tree is empty,
            # return negative infinity as there are no elements
            return float('-inf')
        current = self.root
        # Traverse towards the rightmost node
        while current.right is not None:
            current = current.right
        # the maximum value in the tree
        return current.data

    # Finding the Minimum Value in the Tree
    def find_min(self):
        if self.root is None:
            # If the tree is empty,
            # return infinity as there are no elements
            return float('inf')
        current = self.root
        # Traverse towards the leftmost node
        while current.left is not None:
            current = current.left
        return current.data

    # Searching for a Node:
    def search(self, value):
        return self._search(value, self.root)

    def _search(self, value, node):
        # Check if the current node is None or value
        if node is None or node.data == value:
            return node
        elif value < node.data:
            # If the target value is less than the current node's data,
            # recursively search in the left subtree
            return self._search(value, node.left)
        else:
            # If the target value is greater than the current node's data,
            # recursively search in the right subtree
            return self._search(value, node.right)


# Example usage:
tree = BinaryTree(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

tree.printParent()
tree.print_tree(tree.root)
print("Number of edges in the tree:", tree.count_edges())
tree.print_leaf_nodes()
print("Maximum value in the tree:", tree.find_max())
print("Minimum value in the tree:", tree.find_min())


