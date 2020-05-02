
import unittest

from minimum_2d_path import minimum_2d_path
from rob_houses import rob


class TestSuite(unittest.TestCase):

    def test_minimum_2D_path(self):
        self.assertEqual(0, minimum_2d_path([]))
        self.assertEqual(7, minimum_2d_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
        self.assertEqual(23, minimum_2d_path(
            [[5, 4, 3, 2], [5, 3, 6, 2], [3, 4, 5, 2], [2, 1, 2, 5]]))
        self.assertEqual(1, minimum_2d_path([[1]]))

    def test_rob_houses(self):
        self.assertEqual(4, rob([1, 2, 3, 1]))
        self.assertEqual(15, rob([2, 4, 1, 2, 3, 4, 2, 2, 1, 2, 3]))


if __name__ == "__main__":
    unittest.main()
