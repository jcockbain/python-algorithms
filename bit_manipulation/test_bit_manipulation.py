
import unittest

from hamming_distance import hamming_distance


class TestSuite(unittest.TestCase):

    def test_minimum_2D_path(self):
        self.assertEqual(2, hamming_distance(1, 4))
