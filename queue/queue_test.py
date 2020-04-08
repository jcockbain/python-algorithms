
import unittest

from queue import CircularQueue


class TestSuite(unittest.TestCase):
    def setUp(self):
        self.test_queue = CircularQueue(4)

    def test_queue(self):
        self.assertEqual(-1, self.test_queue.Rear())
        self.assertEqual(-1, self.test_queue.Front())
        self.assertEqual(False, self.test_queue.deQueue())
        self.assertEqual(True, self.test_queue.isEmpty())
        self.test_queue.enQueue(1)
        self.test_queue.enQueue(2)
        self.assertEqual(False, self.test_queue.isFull())
        self.test_queue.enQueue(3)
        self.test_queue.enQueue(4)
        self.assertEqual(False, self.test_queue.enQueue(1))
        self.assertEqual(1, self.test_queue.Front())
        self.assertEqual(True, self.test_queue.isFull())
        self.test_queue.deQueue()
        self.assertEqual(2, self.test_queue.Front())
        self.assertEqual(4, self.test_queue.Rear())
        self.assertEqual(False, self.test_queue.isEmpty())

if __name__ == "__main__":
    unittest.main()
