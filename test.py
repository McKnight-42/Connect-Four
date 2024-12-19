import unittest
from board import create_board, is_board_full
from game import drop_piece
from check_win import check_winner

class TestConnectFour(unittest.TestCase):

    def setUp(self):
        """Set up the board for tests"""
        self.board = create_board()

    def test_drop_piece(self):
        """Test that a piece is correctly dropped into a column."""
        # Drop a red piece into column 3
        drop_piece(self.board, 3, '🔴')
        self.assertEqual(self.board[5][3], '🔴')

        # Drop a yellow piece into column 3
        drop_piece(self.board, 3, '🟡')
        self.assertEqual(self.board[4][3], '🟡')

    def test_check_winner_horizontal(self):
        """Test that a horizontal win is detected."""
        self.board[5] = ['🔴', '🔴', '🔴', '🔴', ' ', ' ', ' ']
        self.assertTrue(check_winner(self.board, '🔴'))

    def test_check_winner_vertical(self):
        """Test that a vertical win is detected."""
        for i in range(4):
            drop_piece(self.board, 3, '🔴')
        self.assertTrue(check_winner(self.board, '🔴'))

    def test_check_winner_diagonal(self):
        """Test that a diagonal win is detected."""
        self.board[5][0] = '🔴'
        self.board[4][1] = '🔴'
        self.board[3][2] = '🔴'
        self.board[2][3] = '🔴'
        self.assertTrue(check_winner(self.board, '🔴'))

    def test_is_board_full(self):
        """Test that a full board is correctly identified."""
        for row in range(6):
            for col in range(7):
                self.board[row][col] = '🔴'
        self.assertTrue(is_board_full(self.board))

if __name__ == '__main__':
    unittest.main()
