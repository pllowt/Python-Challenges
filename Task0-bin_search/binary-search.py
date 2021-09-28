# A tree node class that contains a left and right 'pointer' to the next tree node
class TreeNodeStruct:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: TreeNodeStruct = left
        self.right: TreeNodeStruct = right

    def __str__(self) -> str:
        return f"Value is {self.value}"


def look_up(value) -> bool:
    pass


# This needs to be looked at!
def multiple_insertion(self, *args: TreeNodeStruct):
    pass


def main():
    first_node = TreeNodeStruct(value=10)
    second_node = TreeNodeStruct(value=20)
    multiple_insertion(first_node, second_node)


if __name__ == '__main__':
    main()
