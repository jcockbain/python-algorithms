
import unittest

from tree import TreeNode
from max_depth import maxDepth


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.test_tree_root = TreeNode(1)
        self.test_tree_root.left = TreeNode(2)
        self.test_tree_root.right = TreeNode(3)

    def test_treeNode(self):

        self.assertEqual(2, self.test_tree_root.left.val)
        self.assertEqual(3, self.test_tree_root.right.val)

    def test_maxDepth(self):
        self.assertEqual(2, maxDepth(self.test_tree_root))


if __name__ == "__main__":
    unittest.main()
