import random
import time
from board import create_board, print_board, drop_piece, is_board_full
from validate import get_valid_column
from check_win import check_winner

# Optimized get_winning_move to reduce redundant checks
def get_winning_move(board, piece):
    """Check if a player has a winning move and return the column."""
    for col in range(len(board[0])):
        if board[0][col] == ' ':  # Only check if the column is not full
            for row in reversed(range(len(board))):
                if board[row][col] == ' ':
                    board[row][col] = piece  # Temporarily place the piece
                    if check_winner(board, piece):
                        board[row][col] = ' '  # Undo the move
                        return col
                    board[row][col] = ' '  # Undo the move
                    break
    return None

def get_computer_move(board):
    """AI selects a move, prioritizing blocking and winning."""
    # Check if the computer can win
    move = get_winning_move(board, '🟡')
    if move is not None:
        return move
    
    # Check if the player can win and block it
    move = get_winning_move(board, '🔴')
    if move is not None:
        return move
    
    # If no winning or blocking move, pick a random valid column
    valid_columns = [col for col in range(len(board[0])) if board[0][col] == ' ']
    return random.choice(valid_columns)

def get_game_mode():
    """Prompt players to choose game mode."""
    while True:
        mode = input("Choose game mode:\n1. 2 Human Players\n2. Human vs Computer\nEnter 1 or 2: ").strip()
        if mode == '1' or mode == '2':
            return int(mode)
        else:
            print("Invalid input. Please enter '1' or '2'.")

def play_game():
    game_mode = get_game_mode()  # Get the game mode
    board = create_board()
    game_over = False
    turn = 0  # 0 for Player 1 (Human), 1 for Player 2 (Computer or Human)
    
    while not game_over:
        # Print the current board state
        print_board(board)
        
        if game_mode == 1:  # Two human players
            col = get_valid_column(board, turn)
        else:  # One human player against computer
            if turn == 0:  # Human turn
                col = get_valid_column(board, turn)
            else:  # Computer turn
                print("Computer is thinking...")
                time.sleep(2)  # Add a 2-second delay to simulate thinking
                col = get_computer_move(board)
        
        # Determine the player's piece ('🔴' or '🟡')
        piece = '🔴' if turn == 0 else '🟡'
        
        # Drop the piece in the selected column
        if drop_piece(board, col, piece):
            # Check for a winner
            if check_winner(board, piece):
                print_board(board)
                if turn == 0:
                    print("Player 1 (🔴) wins!")
                else:
                    if game_mode == 1:
                        print("Player 2 (🟡) wins!")
                    else:
                        print("Computer (🟡) wins!")
                game_over = True
            else:
                # Check for a tie (full board)
                if is_board_full(board):
                    print_board(board)
                    print("The game is a draw!")
                    game_over = True
        
        # Switch turns
        turn = (turn + 1) % 2
