def check_horizontal(board, piece):
    for row in range(len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row][col + i] == piece for i in range(4)):
                return True
    return False

def check_vertical(board, piece):
    for col in range(len(board[0])):
        for row in range(len(board) - 3):
            if all(board[row + i][col] == piece for i in range(4)):
                return True
    return False

def check_diagonal(board, piece):
    for row in range(len(board) - 3):
        for col in range(len(board[0]) - 3):
            if all(board[row + i][col + i] == piece for i in range(4)):
                return True
    for row in range(3, len(board)):
        for col in range(len(board[0]) - 3):
            if all(board[row - i][col + i] == piece for i in range(4)):
                return True
    return False

def check_winner(board, piece):
    return check_horizontal(board, piece) or check_vertical(board, piece) or check_diagonal(board, piece)
