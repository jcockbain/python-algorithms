
import unittest

from open_the_lock import openLock


class TestSuite(unittest.TestCase):
    def test_openLock(self):
        deadends = ["0201", "0101", "0102", "1212", "2002"]
        self.assertEqual(6, openLock(deadends, "0202"))

    def test_openLock_2(self):
        deadends = ["8888"]
        self.assertEqual(1, openLock(deadends, "0009"))

    def test_open_impossible_lock(self):
        deadends = ["8887", "8889", "8878",
                    "8898", "8788", "8988", "7888", "9888"]
        self.assertEqual(-1, openLock(deadends, "8888"))
