class TreeNodeStruct:
    def __init__(self, value: int, left: object = None, right: object = None):
        """A class for the nodes of a BST. A tree node contains an integer value, left node and right node.

        Args:
            value (integer): Integer value of the node. 
            left (object, optional): left node object. Defaults to None.
            right (object, optional): right node object. Defaults to None.
        """
        self.value = value
        self.left: TreeNodeStruct = left
        self.right: TreeNodeStruct = right

    def __str__(self) -> str:
        return f"Value is {self.value}"


def look_up(tree_node: TreeNodeStruct, value: int) -> bool:
    """looks up particular value in the BST
    Args:
        tree_node (TreeNodeStruct): [description]
        value (int): [description]

    Returns:
        bool: [description]
    """
    # Base case
    if tree_node is None:
        return False
    # Check value to be searched is less than tree node value. Smaller values on left
    if value < tree_node.value:
        return look_up(tree_node.left, value)
    # Check value to be searched is greater than tree node value. larger values on right
    elif value > tree_node.value:
        return look_up(tree_node.right, value)
    # second base case
    elif value == tree_node.value:
        return True


# Single value insertion
def insertion(tree_node: TreeNodeStruct, value) -> TreeNodeStruct:
    # Base case
    if tree_node is None:
        return TreeNodeStruct(value)
    # Check value is not same as the tree node. If it is return with one value to prevent duplicates
    if tree_node.value != value:
        if value < tree_node.value and not tree_node.left:
            tree_node.left = insertion(tree_node.left, value)
        # Check value to be searched is greater than tree node value. larger values on right
        elif value > tree_node.value and not tree_node.right:
            tree_node.right = insertion(tree_node.right, value)
        elif value > tree_node.value and tree_node.right:
            insertion(tree_node.right, value)
        elif value < tree_node.value and tree_node.left:
            insertion(tree_node.left, value)
    else:
        return tree_node


def deletion():
    # three possibilities
    # 1: Node to be deleted is the leaf; just remove from tree
    # 2: Node to be deleted has only one child; copy child to the node and delete child
    # 3:  Node to be deleted has two children: Find inorder successor of the node.
    #     Copy contents of the inorder successor to the node and delete the inorder successor.
    #     Note that inorder predecessor can also be used. 
    
    # Return True if node found and deleted successfully. 
    # traverse tree to find node
    # if node not found return from function. Return False?
    # if node found:
    # count node children
    pass


def print_tree_in_order(tree_node: TreeNodeStruct):
    if tree_node:
        print_tree_in_order(tree_node.left)
        print(tree_node.value)
        print_tree_in_order(tree_node.right)


def main():
    root_node = TreeNodeStruct(value=5)
    insertion(root_node, 3)
    insertion(root_node, 2)
    insertion(root_node, 4)
    insertion(root_node, 7)
    insertion(root_node, 6)
    insertion(root_node, 8)

    print_tree_in_order(root_node)


if __name__ == '__main__':
    main()
