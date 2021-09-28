# A tree node class that contains a left and right 'pointer' to the next tree node
class TreeNodeStruct:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: TreeNodeStruct = left
        self.right: TreeNodeStruct = right

    def __str__(self) -> str:
        return f"Value is {self.value}"


def look_up(root_node: TreeNodeStruct, value) -> bool:
    # Base case
    if root_node is None:
        return False
    # Check value to be searched is less than tree node value. Smaller values on left
    if value < root_node.value:
        return look_up(root_node.left, value)
    # Check value to be searched is greater than tree node value. larger values on right
    elif value > root_node.value:
        return look_up(root_node.right, value)
    # second base case
    elif value == root_node.value:
        return True


def check_insertion_duplication(root_node: TreeNodeStruct, insertion_node: TreeNodeStruct) -> bool:
    if look_up(root_node, insertion_node.value):
        return False
    else:
        return True


def insertion():
    pass


# This needs to be looked at!
def multiple_insertion(*args: TreeNodeStruct):
    pass


def main():
    first_node = TreeNodeStruct(value=10)
    second_node = TreeNodeStruct(value=20)
    multiple_insertion(first_node, second_node)


if __name__ == '__main__':
    main()
