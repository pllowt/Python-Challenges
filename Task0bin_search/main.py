import binarysearchtree as BST


def main():
    root_node = BST.TreeNode(value=5)
    BST.inserts_node(root_node, 3)
    BST.inserts_node(root_node, 2)
    BST.inserts_node(root_node, 4)
    BST.inserts_node(root_node, 7)
    BST.inserts_node(root_node, 6)
    BST.inserts_node(root_node, 8)

    BST.print_tree_in_order(root_node)


if __name__ == '__main__':
    main()