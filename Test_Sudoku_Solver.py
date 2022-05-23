from logging import exception
import unittest
from unittest import mock

from Sudoku_Solver import sudoku_board


class TestSudokuSolver(unittest.TestCase):

    # Test if file patch to .txt file is proper
    def test_proper_file(self):
        with self.assertRaises(Exception):
            sudoku_board("./Test_board_example2.txt")

    # Check check_row function
    def test_check_row_True(self):
        check = sudoku_board("./Test_board_example.txt")
        self.assertEqual(check.check_rows(1, 0), True)

    def test_check_row_False(self):
        check = sudoku_board("./Test_board_example.txt")
        self.assertEqual(check.check_rows(5, 0), False)

    # Check check_column function
    def test_check_column_True(self):
        check = sudoku_board("./Test_board_example.txt")
        self.assertEqual(check.check_columns(1, 0), True)

    def test_check_column_False(self):
        check = sudoku_board("./Test_board_example.txt")
        self.assertEqual(check.check_columns(5, 0), False)

    # Check segment function
    def test_check_segment_True(self):
        check = sudoku_board("./Test_board_example.txt")
        self.assertEqual(check.check_segment(1, 0, 0), True)

    def test_check_column_False(self):
        check = sudoku_board("./Test_board_example.txt")
        self.assertEqual(check.check_segment(3, 0, 0), False)
