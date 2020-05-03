import unittest

from valid_parentheses import isValid


class TestSuite(unittest.TestCase):
    def test_valid_parenthese(self):
        self.assertTrue(isValid("({})"))
        self.assertTrue(isValid("({[]})"))
        self.assertFalse(isValid("(()}"))
        self.assertFalse(isValid("({[]}"))
