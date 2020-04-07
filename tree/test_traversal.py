
import unittest

from tree import TreeNode
from preorder_traversal import preorder_traversal
from inorder_traversal import inorder_traversal


class TestSuite(unittest.TestCase):
    def test_preorder(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)

        self.assertEqual([3,2,1,4], preorder_traversal(root))

    def test_inorder(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.right = TreeNode(4)
        root.left.left = TreeNode(1)

        self.assertEqual([1,2,3,4], inorder_traversal(root))




if __name__ == "__main__":
    unittest.main()
