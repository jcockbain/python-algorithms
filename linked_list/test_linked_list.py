import unittest

from Node import Node
from LinkedList import LinkedList
from add_two_numbers import add_two_numbers
from reverse_linked_list import reverseList


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.test_ll_head_1 = Node(0)
        self.test_ll_head_1.next = Node(1)
        self.test_ll_head_1.next.next = Node(2)

        self.test_ll_head_2 = Node(2)
        self.test_ll_head_2.next = Node(3)
        self.test_ll_head_2.next.next = Node(4)

    def test_node(self):
        head = self.test_ll_head_1
        self.assertEqual(head.next.next.val, 2)

    def test_add_two_numbers(self):
        ans = add_two_numbers(self.test_ll_head_1, self.test_ll_head_2)
        self.assertEqual(2, ans.val)
        self.assertEqual(4, ans.next.val)
        self.assertEqual(6, ans.next.next.val)

        h3 = Node(5)
        h4 = Node(5)
        ans2 = add_two_numbers(h3, h4)
        self.assertEqual(0, ans2.val)
        self.assertEqual(1, ans2.next.val)

    def test_reverse_linked_list(self):
        ans = reverseList(self.test_ll_head_1)
        self.assertEqual(2, ans.val)
        self.assertEqual(1, ans.next.val)
        self.assertEqual(0, ans.next.next.val)

    def test_linked_list(self):
        ll = LinkedList()
        self.assertEqual(True, ll.is_empty())
        ll.insert_at_head(1)
        self.assertEqual(False, ll.is_empty())
        ll.insert_at_head(2)
        self.assertEqual(True, ll.print_list())
