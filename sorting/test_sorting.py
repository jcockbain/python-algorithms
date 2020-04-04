import unittest

from insertion_sort import insertion_sort
from selection_sort import selection_sort


class TestSuite(unittest.TestCase):
    def test_sort_1(self):
        arr = [5, 1, 2, 3, 4]
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(expected, insertion_sort(arr))
        self.assertEqual(expected, selection_sort(arr))

    def test_sort_2(self):
        arr = [5, 2, 2, 3, 4, 5]
        expected = [2, 2, 3, 4, 5, 5]
        self.assertEqual(expected, insertion_sort(arr))
        self.assertEqual(expected, selection_sort(arr))

    def test_sort_3(self):
        arr = [5, 4, -3, 2, 1, 0]
        expected = [-3, 0, 1, 2, 4, 5]
        self.assertEqual(expected, insertion_sort(arr))
        self.assertEqual(expected, selection_sort(arr))

    def test_sort_4(self):
        arr = [1] * 5
        expected = [1] * 5
        self.assertEqual(expected, insertion_sort(arr))
        self.assertEqual(expected, selection_sort(arr))


if __name__ == "__main__":
    unittest.main()
