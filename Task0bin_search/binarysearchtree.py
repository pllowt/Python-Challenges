"""Program to create a Binary Search Tree (BST) and associated functions
"""
class BST:
    """Main BST Class

    Returns:
        Object: BST object with left and right nodes 
    """
    def __init__(self, value: int = 0, left: object = None, right: object = None):
        """init constructor returns node with left and right node objects defaulted to None.

        Args:
            value (integer): Integer value of the node. Defaults to 0. 
            left (object, optional): left node object. Defaults to None.
            right (object, optional): right node object. Defaults to None.
        """
        self.value = value
        self.left: BST = left
        self.right: BST = right
        
            
    def insert_node_obj_into_bst(self, value: int, tree_node: object):
        """Recursive function that inserts node into the tree
        """
        # Base case
        if tree_node is None:
            return BST(value)
        else:
            if tree_node.value == value:
                return tree_node
            elif value < tree_node.value:
                tree_node.left = self.insert_node_obj_into_bst(value, tree_node.left)
            elif value > tree_node.value:
                tree_node.right = self.insert_node_obj_into_bst(value, tree_node.right)
        return tree_node
            
  
    
    def look_up_value(self, tree_node: object, value: int) -> bool:
        """looks up particular value in the BST
        Args:
            tree_node (object): 
            value (int): Integer Node value

        Returns:
            bool: returns True if value is in tree
        """
        # Base case
        if tree_node is None:
            return False
        # Check value to be searched is less than tree node value. Smaller values on left
        if value < tree_node.value:
            return self.look_up_value(tree_node.left, value)
        # Check value to be searched is greater than tree node value. larger values on right
        elif value > tree_node.value:
            return self.look_up_value(tree_node.right, value)
        # second base case
        elif value == tree_node.value:
            return True

def deletes_node(tree_node: BST, value: int):
    """Deletes particular value in the BST

    Args:
        tree_node (BST):
        value (int): Integer Node value
    """
    # Base case:
    if tree_node is None:
        return tree_node
    
    # Conditional statements for checking Node value against arg value
    if value < tree_node.value:
        tree_node.left = deletes_node(tree_node.left, value)
    elif value > tree_node.value:
        tree_node.right = deletes_node(tree_node.right, value)
    else:
        # Cases 1 and 2: Node with one or no children
        if tree_node.left is None:
            temporary_node = tree_node.right
            tree_node = None
            return temporary_node
        elif tree_node.right is None:
            temporary_node = tree_node.left
            tree_node = None
            return temporary_node
        
        # Case 3 : Node with two children
        temporary_node = find_maximum_in_tree(tree_node.left)
        # set current node's value to temporary node's value
        tree_node.value = temporary_node.value

        tree_node.left = deletes_node(tree_node.left, temporary_node.value)
    return tree_node

    def __str__(self) -> str:
        return f"Value is {self.value}"


def find_maximum_in_tree(tree_node):
    current_node = tree_node
    # loop to find the largest value in subtree
    while(current_node.right is not None):
        current_node = current_node.right
    return current_node


def print_tree_in_order(tree_node: BST):
    if tree_node:
        print_tree_in_order(tree_node.left)
        print(tree_node.value)
        print_tree_in_order(tree_node.right)


def main():
    root_node = BST(10)
    print(root_node)
    root_node.insert_node_obj_into_bst(20, root_node)
    root_node.insert_node_obj_into_bst(6, root_node)
    root_node.insert_node_obj_into_bst(9, root_node)
    value_in_tree = root_node.look_up_value(root_node, 9)
    print(value_in_tree)
    print_tree_in_order(root_node)


if __name__ == '__main__':
    main()