import unittest

from linked_list import Node
from add_two_numbers import add_two_numbers


class TestSuite(unittest.TestCase):
    def test_add_two_numbers(self):
        h1 = Node(1)
        h1.next = Node(2)
        h1.next.next = Node(3)

        h2 = Node(2)
        h2.next = Node(3)
        h2.next.next = Node(6)

        ans = add_two_numbers(h1, h2)
        self.assertEqual(3, ans.val)
        self.assertEqual(5, ans.next.val)
        self.assertEqual(9, ans.next.next.val)


if __name__ == "__main__":
    unittest.main()
