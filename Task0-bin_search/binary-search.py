# A tree node class that contains a left and right 'pointer' to the next tree node
class TreeNodeStruct:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left: TreeNodeStruct = left
        self.right: TreeNodeStruct = right

    def __str__(self) -> str:
        return f"Value is {self.value}"


class BinarySearchTree:
    def __init__(self):
        pass

    # This needs to be looked at!
    def insertion(self, *args: TreeNodeStruct):
        # *args returns a tuple
        if len(args) == 0:
            print("Usage: insertion(...)")
            exit(1)

        '''
        check to see if any of the args are not of type TreeNodeStruct
        if not, exit with error code 1
        '''
        for item in args:
            if type(item) is not TreeNodeStruct:
                print("Usage: insertion (arg) not of type TreeNodeStruct")
                exit(1)



def main():
    first_node = TreeNodeStruct(value=10)
    second_node = TreeNodeStruct(value=20)
    tree = BinarySearchTree()
    tree.insertion(first_node, second_node)


if __name__ == '__main__':
    main()
