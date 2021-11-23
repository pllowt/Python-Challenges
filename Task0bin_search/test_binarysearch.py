import unittest
from binarysearchtree import BST

class TestBinSearchTree(unittest.TestCase):
    def test_binary_search_tree_instantiates(self):
        try:
            BST()
        except NameError:
            self.fail("BST could not be instantiated")
    
    def test_initial_attributes_instantiate_to_none(self):
        node = BST()
        self.assertEqual(node.left, None)
        self.assertEqual(node.right, None)
    
    def test_initial_instantiates_with_integer_value(self):
        node = BST(value=99)
        self.assertEqual(99, node.value)
        
    def test_initial__throws_error_instantiates_with_noninteger_value(self):
        try:
            BST(value="'tis but a scratch!")
        except TypeError:
            self.fail("BST only accepts integer values")
    
    def test_look_up_value_returns_true_if_value_in_tree(self):
        test_root_node = initialise_tree()
        self.assertEqual(test_root_node.look_up_value(10, test_root_node), True)

    def test_look_up_value_returns_false_if_value_not_in_tree(self):
        test_root_node = initialise_tree()
        self.assertEqual(test_root_node.look_up_value(42, test_root_node), False)
        
    def test_deletes_node_deletes_node_in_tree(self):
        test_root_node = initialise_tree()
        test_root_node.deletes_node(9, test_root_node)
        self.assertEqual(test_root_node.look_up_value(9, test_root_node), False)
        

# Helper function for initialising TreeNodes
def initialise_tree() -> BST:
    root_node = BST(value=10)
    root_node.insert_node_obj_into_bst(2, root_node)
    root_node.insert_node_obj_into_bst(6, root_node)
    root_node.insert_node_obj_into_bst(5, root_node)
    root_node.insert_node_obj_into_bst(3, root_node)
    root_node.insert_node_obj_into_bst(9, root_node)
    root_node.insert_node_obj_into_bst(1, root_node)
    root_node.insert_node_obj_into_bst(10, root_node)
    value_in_tree = root_node.look_up_value(6, root_node)
    return root_node