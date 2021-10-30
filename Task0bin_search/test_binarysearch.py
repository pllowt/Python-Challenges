import unittest
from binarysearch import TreeNodeStruct
from binarysearch  import look_up
from binarysearch  import insertion

class TestBinSearchTree(unittest.TestCase):
    def test_lookup_func_returns_true(self):
        test_node1 = TreeNodeStruct(value=10)
        test_node2 = TreeNodeStruct(value=50, left= test_node1)
        test_noderoot = TreeNodeStruct(value=500, left= test_node2)
        self.assertEqual(look_up(test_noderoot, 10), True)

    def test_lookup_false(self):
        test_node1 = TreeNodeStruct(value=10)
        test_node2 = TreeNodeStruct(value=50, left= test_node1)
        test_node3 = TreeNodeStruct(value=600, left=test_node1)
        test_noderoot = TreeNodeStruct(value=500, left=test_node2, right=test_node3)
        self.assertEqual(look_up(test_noderoot, 700), False)

    def test_insertion_for_duplicates(self):
        # try to initialise a tree with duplicates
        root_node = TreeNodeStruct(value=5)
        insertion(root_node, 3)
        insertion(root_node, 3)
        insertion(root_node, 4)
        insertion(root_node, 7)
        insertion(root_node, 7)
        insertion(root_node, 7)
        insertion(root_node, 8)
        self.assertEqual(check_insertion_duplication(root_node, 9), False)

# Helper function for testing duplication
def check_insertion_duplication(tree_node: TreeNodeStruct, value) -> bool:
    if look_up(tree_node, value):
        return False
    else:
        return True