
import unittest

from hamming_distance import hamming_distance
from hamming_weight import hamming_weight
from number_complement import find_complement


class TestSuite(unittest.TestCase):

    def test_hamming_distance(self):
        self.assertEqual(2, hamming_distance(1, 4))

    def test_hamming_weight(self):
        self.assertEqual(3, hamming_weight(11))

    def test_find_complement(self):
        self.assertEqual(2, find_complement(5))
