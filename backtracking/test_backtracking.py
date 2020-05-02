import unittest

from n_queens import totalNQueens


class TestSuite(unittest.TestCase):
    def test_nQueens(self):
        self.assertEqual(2, totalNQueens(4))
        self.assertEqual(92, totalNQueens(8))
        self.assertEqual(1, totalNQueens(1))
        self.assertEqual(40, totalNQueens(7))


if __name__ == "__main__":
    unittest.main()
