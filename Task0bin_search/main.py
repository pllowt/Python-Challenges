import binarysearchtree as bst


def main():
    root_node = bst.BST(10)
    print(root_node)
    root_node.inserts_node(20, root_node)
    
    """print('Tree before deletion')
    BST.print_tree_in_order(root_node)
    print('Tree after deletion')
    BST.deletes_node(root_node, 8)
    BST.print_tree_in_order(root_node)
    print('Tree after deletion 2')
    BST.deletes_node(root_node, 2)
    BST.print_tree_in_order(root_node)"""


if __name__ == '__main__':
    main()