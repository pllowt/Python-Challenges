import unittest
from binarysearchtree import TreeNode
from binarysearchtree import looks_up_value
from binarysearchtree import inserts_node

class TestBinSearchTree(unittest.TestCase):
    def test_binary_search_tree_instantiates(self):
        try:
            TreeNode()
        except NameError:
            self.fail("BST could not be instantiated")
    
    def test_initial_attributes_instantiate_to_none(self):
        node = TreeNode()
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)
    
    def test_initial_instantiates_with_integer_value(self):
        node = TreeNode(value=99)
        self.assertEqual(99, node.value)
        
    def test_initial__throws_error_instantiates_with_noninteger_value(self):
        try:
            TreeNode(value="'tis but a scratch!")
        except TypeError:
            self.fail("BST only accepts integer values")
    
    def test_looks_up_value_returns_true_if_value_in_tree(self):
        test_node1 = TreeNode(value=10)
        test_node2 = TreeNode(value=50, left= test_node1)
        test_noderoot = TreeNode(value=500, left= test_node2)
        self.assertEqual(looks_up_value(test_noderoot, 10), True)

    def test_looks_up_value_returns_false_if_value_not_in_tree(self):
        test_node1 = TreeNode(value=10)
        test_node2 = TreeNode(value=50, left= test_node1)
        test_noderoot = TreeNode(value=500, left=test_node1, right=test_node2)
        self.assertEqual(looks_up_value(test_noderoot, 700), False)
        
def test_delete_deletes_node_in_tree_without_removing_its_children(self):
        test_node1 = TreeNode(value=10)
        test_node2 = TreeNode(value=50, left= test_node1)
        test_noderoot = TreeNode(value=500, left=test_node1, right=test_node2)
        self.assertEqual(looks_up_value(test_noderoot, 700), False)
        


# Helper function for initialising TreeNodes
# def initialise_tree():
#     test_node1 = TreeNode(value=10)
#     test_node2 = TreeNode(value=50, left= test_node1)
#     test_node3 = TreeNode(value=600, left=test_node2)
#     return list(test_node1, test_node2, test_node3)

# Helper function for testing duplication
# def check_inserts_node_duplication(tree_node: TreeNode, value) -> bool:
#     if looks_up_value(tree_node, value):
#         return False
#     else:
#         return True