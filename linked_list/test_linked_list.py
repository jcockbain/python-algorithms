import unittest

from linked_list import Node


class TestSuite(unittest.TestCase):
    def test_node(self):
        head = Node(0)
        head.next = Node(1)
        head.next.next = Node(2)

        self.assertEqual(head.next.next.val, 2)


if __name__ == "__main__":
    unittest.main()
