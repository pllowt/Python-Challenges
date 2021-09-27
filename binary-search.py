

class TreeNodeStruct:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: TreeNodeStruct = left
        self.right: TreeNodeStruct = right

    def __str__(self):
        return f"Value is {self.value}"


class BinarySearchTree:
    def __init__(self):
        pass

    # This needs to be looked at!
    def insertion(self, *args: TreeNodeStruct):
        # *args returns a tuple
        if len(args) == 0:
            print("Usage: insertion(...)")
            return
        for item in args:
            if item.value < item + 1:
                print(item.value)



def main():
    first_node = TreeNodeStruct(value=10)
    second_node = TreeNodeStruct(value=20)
    tree = BinarySearchTree()
    tree.insertion(first_node, second_node)


if __name__ == '__main__':
    main()
