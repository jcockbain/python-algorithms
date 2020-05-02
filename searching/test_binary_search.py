import unittest

from binary_search import binary_search


class TestSuite(unittest.TestCase):
    def test_1(self):
        arr = [1, 2, 3, 4, 6]
        self.assertEqual(2, binary_search(arr[:], 0, len(arr) - 1, 3))
        self.assertEqual(-1, binary_search(arr[:], 0, len(arr) - 1, 5))

    def test_2(self):
        arr = [1, 2, 2, 3, 4, 6]
        self.assertEqual(0, binary_search(arr[:], 0, len(arr) - 1, 1))
