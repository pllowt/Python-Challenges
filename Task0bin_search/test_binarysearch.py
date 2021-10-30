import unittest
from binarysearch import TreeNodeStruct
from binarysearch import looks_up_value
from binarysearch import inserts_node

class TestBinSearchTree(unittest.TestCase):
    def test_binary_search_tree_instantiates_with_value(self):
        try:
            TreeNodeStruct(value=1)
        except NameError:
            self.fail("BST could not be instantiated")
    
    def test_initial_node_pointer_attributes_exist_are_none(self):
        node = TreeNodeStruct(value=1)
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)
    
    def test_looks_up_value_returns_true_if_value_in_tree(self):
        test_node1 = TreeNodeStruct(value=10)
        test_node2 = TreeNodeStruct(value=50, left= test_node1)
        test_noderoot = TreeNodeStruct(value=500, left= test_node2)
        self.assertEqual(looks_up_value(test_noderoot, 10), True)

    def test_looks_up_value_returns_false_if_value_in_tree(self):
        test_node1 = TreeNodeStruct(value=10)
        test_node2 = TreeNodeStruct(value=50, left= test_node1)
        test_node3 = TreeNodeStruct(value=600, left=test_node1)
        test_noderoot = TreeNodeStruct(value=500, left=test_node2, right=test_node3)
        self.assertEqual(looks_up_value(test_noderoot, 700), False)

    # def test_inserts_node_for_duplicates(self):
    #     # try to initialise a tree with duplicates
    #     root_node = TreeNodeStruct(value=5)
    #     inserts_node(root_node, 3)
    #     inserts_node(root_node, 3)
    #     inserts_node(root_node, 4)
    #     inserts_node(root_node, 7)
    #     inserts_node(root_node, 7)
    #     inserts_node(root_node, 7)
    #     inserts_node(root_node, 8)
    #     self.assertEqual(check_inserts_node_duplication(root_node, 9), False)

# # Helper function for testing duplication
# def check_inserts_node_duplication(tree_node: TreeNodeStruct, value) -> bool:
#     if looks_up_value(tree_node, value):
#         return False
#     else:
#         return True