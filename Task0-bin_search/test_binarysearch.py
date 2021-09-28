import unittest
from binarysearch import TreeNodeStruct
from binarysearch import look_up

class TestBinSearchTree(unittest.TestCase):
    def test_lookup_true(self):
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