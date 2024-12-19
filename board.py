ROWS = 6
COLS = 7

def create_board():
    return [[' ' for _ in range(COLS)] for _ in range(ROWS)]

def print_board(board):
    for row_idx, row in enumerate(board):
        print(f"{row_idx} |" + '|'.join(row) + f"|")
    print(' ' + '-' * (COLS * 2 + 3))
    print('  ' + ' '.join(f'{i}' for i in range(COLS)))

def drop_piece(board, col, piece):
    for row in reversed(range(ROWS)):
        if board[row][col] == ' ':
            board[row][col] = piece
            return True
    return False

def is_board_full(board):
    return all(board[0][col] != ' ' for col in range(COLS))
