# A tree node class that contains a left and right 'pointer' to the next tree node
class TreeNodeStruct:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: TreeNodeStruct = left
        self.right: TreeNodeStruct = right

    def __str__(self) -> str:
        return f"Value is {self.value}"


def look_up(tree_node: TreeNodeStruct, value) -> bool:
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


def check_insertion_duplication(tree_node: TreeNodeStruct, value) -> bool:
    if look_up(tree_node, value):
        return False
    else:
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
