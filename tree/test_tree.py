
import unittest

from tree import TreeNode


class TestSuite(unittest.TestCase):
    def test_sort(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(2, root.left.val)
        self.assertEqual(3, root.right.val)


if __name__ == "__main__":
    unittest.main()
