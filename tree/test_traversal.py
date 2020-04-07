
import unittest

from tree import TreeNode
from preorder_traversal import preorder_traversal


class TestSuite(unittest.TestCase):
    def test_preorder(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)

        self.assertEqual([3,2,1,4], preorder_traversal(root))




if __name__ == "__main__":
    unittest.main()
