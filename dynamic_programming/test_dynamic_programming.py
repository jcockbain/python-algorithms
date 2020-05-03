
import unittest

from minimum_2d_path import minimum_2d_path
from rob_houses import rob, rob2
from jump_game import canJump1, canJump2, canJump3
from climb_stairs import climb1, climb2, climb3


class TestSuite(unittest.TestCase):

    def test_minimum_2D_path(self):
        self.assertEqual(0, minimum_2d_path([]))
        self.assertEqual(7, minimum_2d_path([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))
        self.assertEqual(23, minimum_2d_path(
            [[5, 4, 3, 2], [5, 3, 6, 2], [3, 4, 5, 2], [2, 1, 2, 5]]))
        self.assertEqual(1, minimum_2d_path([[1]]))

    def test_rob_houses(self):
        self.assertEqual(4, rob([1, 2, 3, 1]))
        self.assertEqual(15, rob([2, 4, 1, 2, 3, 4, 2, 2, 1, 2, 3]))

        self.assertEqual(4, rob2([1, 2, 3, 1]))
        self.assertEqual(15, rob2([2, 4, 1, 2, 3, 4, 2, 2, 1, 2, 3]))

    def test_jump_game(self):
        self.assertEqual(True, canJump1([2, 3, 1, 1, 4]))
        self.assertEqual(False, canJump1([3, 2, 1, 0, 4]))

        self.assertEqual(True, canJump2([2, 3, 1, 1, 4]))
        self.assertEqual(False, canJump2([3, 2, 1, 0, 4]))

        self.assertEqual(True, canJump3([2, 3, 1, 1, 4]))
        self.assertEqual(False, canJump3([3, 2, 1, 0, 4]))

    def test_climb_stairs(self):
        self.assertEqual(1, climb1(1))
        self.assertEqual(987, climb1(15))
        self.assertEqual(1, climb1(1))
        self.assertEqual(987, climb2(15))
        self.assertEqual(1, climb3(1))
        self.assertEqual(987, climb3(15))
