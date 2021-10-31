"""Script to create a Binary Search Tree

    Returns:
        Object: TreeNode object which has a root node and pointer to left and right nodes.
"""
class TreeNode:
    # Init instance variables for TreeNode
    def __init__(self, value: int = None, left: object = None, right: object = None):
        """Class for the nodes of a BST. A tree node contains an integer value, left node and right node.

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



def delete_node(tree_node: TreeNode, value: int):
    # three possibilities
    # 1: Node to be deleted is the leaf; just remove from tree
    # 2: Node to be deleted has only one child; copy child to the node and delete child
    # 3:  Node to be deleted has two children: Find inorder successor of the node.
    #     Copy contents of the inorder successor to the node and delete the inorder successor.
    #     Note that inorder predecessor can also be used. 
    # Above from https://www.geeksforgeeks.org/binary-search-tree-set-2-delete/ 
    
    # Return True if node found and deleted successfully. 
    # traverse tree to find node
    # if node not found return from function. Return False?
    # if node found:
    # count node children
    # Base case:
    if tree_node is None:
        return tree_node
    
    # Conditional statements for checking Node value against arg value
    # check if value is less than the TreeNode value 
    if value < TreeNode.value:
        delete_node(tree_node, value)
    pass


def print_tree_in_order(tree_node: TreeNode):
    if tree_node:
        print_tree_in_order(tree_node.left)
        print(tree_node.value)
        print_tree_in_order(tree_node.right)
