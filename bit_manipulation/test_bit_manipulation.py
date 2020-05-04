
import unittest

from hamming_distance import hamming_distance
from hamming_weight import hamming_weight


class TestSuite(unittest.TestCase):

    def test_hamming_distance(self):
        self.assertEqual(2, hamming_distance(1, 4))

    def test_hamming_weight(self):
        self.assertEqual(3, hamming_weight(11))
