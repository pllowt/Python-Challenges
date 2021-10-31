"""Script to create a Binary Search Tree and associated functions
"""
class TreeNode:
    """Main TreeNode Class

    Returns:
        Object: TreeNode object with left and right nodes 
    """
    def __init__(self, value: int = None, left: object = None, right: object = None):
        """init constructor returns node with left and right node objects defaulted to None.

        Args:
            value (integer): Integer value of the node. Defaults to None. 
            left (object, optional): left node object. Defaults to None.
            right (object, optional): right node object. Defaults to None.
        """
        self.value = value
        self.left: TreeNode = left
        self.right: TreeNode = right

    def __str__(self) -> str:
        return f"Value is {self.value}"
    
    
def inserts_node(tree_node: TreeNode, value: int) -> TreeNode:
    """Recursive function that inserts node into the tree
    """
    # Base case
    if tree_node is None:
        return TreeNode(value)
    # Check value is not same as the tree node. If it is, return with one value to prevent duplicates
    if tree_node.value != value:
        if value < tree_node.value and not tree_node.left:
            tree_node.left = inserts_node(tree_node.left, value)
        # Check value to be searched is greater than tree node value. larger values on right
        elif value > tree_node.value and not tree_node.right:
            tree_node.right = inserts_node(tree_node.right, value)
        elif value > tree_node.value and tree_node.right:
            inserts_node(tree_node.right, value)
        elif value < tree_node.value and tree_node.left:
            inserts_node(tree_node.left, value)
    else:
        return tree_node


def looks_up_value(tree_node: TreeNode, value: int) -> bool:
    """looks up particular value in the BST
    Args:
        tree_node (TreeNode): 
        value (int): Integer Node value

    Returns:
        bool: returns True if value is in tree
    """
    # Base case
    if tree_node is None:
        return False
    # Check value to be searched is less than tree node value. Smaller values on left
    if value < tree_node.value:
        return looks_up_value(tree_node.left, value)
    # Check value to be searched is greater than tree node value. larger values on right
    elif value > tree_node.value:
        return looks_up_value(tree_node.right, value)
    # second base case
    elif value == tree_node.value:
        return True


def deletes_node(tree_node: TreeNode, value: int):
    """Deletes particular value in the BSR

    Args:
        tree_node (TreeNode):
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


def find_maximum_in_tree(tree_node):
    current_node = tree_node
    # loop to find the largest value in subtree
    while(current_node.right is not None):
        current_node = current_node.right
    return current_node

def print_tree_in_order(tree_node: TreeNode):
    if tree_node:
        print_tree_in_order(tree_node.left)
        print(tree_node.value)
        print_tree_in_order(tree_node.right)

