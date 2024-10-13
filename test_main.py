# Import the necessary functions and constants from the Tic Tac Toe code
import unittest
from main import EMPTY_CELL, minimax_ab



class TestMinimaxAB(unittest.TestCase):
    def test_initial_board(self):
        board = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), True), 0)

    def test_immediate_win(self):
        board = [['O', 'O', ' '],
                 ['X', 'X', ' '],
                 [' ', ' ', ' ']]
        # Assuming O is the maximizer and it's O's turn
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), True), 1)

    def test_immediate_loss(self):
        board = [['X', 'X', ' '],
                 ['O', 'O', ' '],
                 [' ', ' ', ' ']]
        # Assuming X is the minimizer and it's X's turn
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), False), -1)

    def test_draw_scenario(self):
        board = [['X', 'O', 'X'],
                 ['X', 'X', 'O'],
                 ['O', 'X', 'O']]
        # No moves left, should be a draw
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), True), 0)
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), False), 0)

    def test_best_move_for_o(self):
        board = [['X', 'O', 'X'],
                 ['O', 'X', ' '],
                 [' ', ' ', ' ']]
        # Best move for O to block X's win
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), True), -1)

    def test_best_move_for_x(self):
        board = [['O', 'X', ' '],
                 ['X', 'O', ' '],
                 [' ', ' ', 'X']]
        # Best move for X to proceed towards a win or draw
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), False), 0)

    def test_o_winning_move(self):
        board = [['O', 'O', ' '],
                 ['X', 'X', 'O'],
                 ['X', ' ', ' ']]
        # O has a winning move
        self.assertEqual(minimax_ab(board, float('-inf'), float('inf'), True), 1)


if __name__ == "__main__":
    unittest.main()