import binarysearchtree as BST


def main():
    root_node = BST.TreeNode(value=5)
    BST.inserts_node(root_node, 3)
    BST.inserts_node(root_node, 2)
    BST.inserts_node(root_node, 4)
    BST.inserts_node(root_node, 7)
    BST.inserts_node(root_node, 6)
    BST.inserts_node(root_node, 8)
    BST.inserts_node(root_node, 100)
    
    print('Tree before deletion')
    BST.print_tree_in_order(root_node)
    print('Tree after deletion')
    BST.deletes_node(root_node, 8)
    BST.print_tree_in_order(root_node)
    print('Tree after deletion 2')
    BST.deletes_node(root_node, 2)
    BST.print_tree_in_order(root_node)


if __name__ == '__main__':
    main()