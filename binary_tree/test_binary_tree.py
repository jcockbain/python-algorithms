
import unittest

from tree import TreeNode
from max_depth import maxDepth
from min_depth import minDepth


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.test_tree_root = TreeNode(1)
        self.test_tree_root.left = TreeNode(2)
        self.test_tree_root.right = TreeNode(3)
        self.test_tree_root.right.right = TreeNode(4)

    def test_treeNode(self):

        self.assertEqual(2, self.test_tree_root.left.val)
        self.assertEqual(3, self.test_tree_root.right.val)

    def test_maxDepth(self):
        self.assertEqual(3, maxDepth(self.test_tree_root))

    def test_minDepth(self):
        self.assertEqual(2, minDepth(self.test_tree_root))
        self.assertEqual(0, minDepth(None))
