import unittest

from insertion_sort import insertion_sort
from selection_sort import selection_sort


class TestSuite(unittest.TestCase):
    def test_sort(self):
        arr = [5, 1, 2, 3, 4]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, insertion_sort(arr))
        self.assertEqual(expected, selection_sort(arr))


if __name__ == "__main__":
    unittest.main()
