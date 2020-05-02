import unittest

from n_queens import totalNQueens
from sudoku_solver import solveSudoku
from generate_parentheses import generateParenthese


class TestSuite(unittest.TestCase):
    def test_nQueens(self):
        self.assertEqual(2, totalNQueens(4))
        self.assertEqual(92, totalNQueens(8))
        self.assertEqual(1, totalNQueens(1))
        self.assertEqual(40, totalNQueens(7))

    def test_sudoku_solver(self):
        sudoku = [["5", "3", ".", ".", "7", ".", ".", ".", "."],
                  ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."],
                  ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                  ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."],
                  [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

        solvedSudoku = [["5", "3", "4", "6", "7", "8", "9", "1", "2"],
                        ["6", "7", "2", "1", "9", "5", "3", "4", "8"],
                        ["1", "9", "8", "3", "4", "2", "5", "6", "7"],
                        ["8", "5", "9", "7", "6", "1", "4", "2", "3"],
                        ["4", "2", "6", "8", "5", "3", "7", "9", "1"],
                        ["7", "1", "3", "9", "2", "4", "8", "5", "6"],
                        ["9", "6", "1", "5", "3", "7", "2", "8", "4"],
                        ["2", "8", "7", "4", "1", "9", "6", "3", "5"],
                        ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

        self.assertEqual(solvedSudoku, solveSudoku(sudoku))

    def test_generate_parenthese(self):
        self.assertEqual(["((()))", "(()())", "(())()",
                          "()(())", "()()()"], generateParenthese(3))
