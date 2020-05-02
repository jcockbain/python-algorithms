
import unittest

from tree import TreeNode
from preorder_traversal import preorder_traversal, preorder_traversal_iterative
from inorder_traversal import inorder_traversal, inorder_traversal_iterative
from postorder_traversal import postorder_traversal, postorder_traversal_iterative
from levelorder_traversal import levelorder_traversal, levelorder_traversal_iterative


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.test_tree_root = TreeNode(3)
        self.test_tree_root.left = TreeNode(2)
        self.test_tree_root.right = TreeNode(4)
        self.test_tree_root.left.left = TreeNode(1)

    def test_preorder(self):
        self.assertEqual([3, 2, 1, 4], preorder_traversal(self.test_tree_root))
        self.assertEqual(
            [3, 2, 1, 4], preorder_traversal_iterative(self.test_tree_root))
        self.assertEqual([], preorder_traversal(None))
        self.assertEqual([], preorder_traversal_iterative(None))

    def test_inorder(self):
        self.assertEqual([1, 2, 3, 4], inorder_traversal(self.test_tree_root))
        self.assertEqual(
            [1, 2, 3, 4], inorder_traversal_iterative(self.test_tree_root))
        self.assertEqual([], inorder_traversal(None))
        self.assertEqual([], inorder_traversal_iterative(None))

    def test_postorder(self):
        self.assertEqual(
            [1, 2, 4, 3], postorder_traversal(self.test_tree_root))
        self.assertEqual(
            [1, 2, 4, 3], postorder_traversal_iterative(self.test_tree_root))
        self.assertEqual([], postorder_traversal(None))
        self.assertEqual([], postorder_traversal_iterative(None))

    def test_levelorder(self):
        self.assertEqual(
            [[3], [2, 4], [1]], levelorder_traversal_iterative(self.test_tree_root))
        self.assertEqual(
            [[3], [2, 4], [1]], levelorder_traversal(self.test_tree_root))
        self.assertEqual([], levelorder_traversal(None))
        self.assertEqual([], levelorder_traversal_iterative(None))
