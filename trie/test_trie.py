import unittest

from trie import Trie


class TestSuite(unittest.TestCase):
    def test_1(self):
        newTree = Trie()
        newTree.insert("hello")
        self.assertTrue(newTree.search("hello"))
        self.assertTrue(newTree.startsWith("hel"))
        self.assertFalse(newTree.search("bye"))
        self.assertFalse(newTree.startsWith("b"))
