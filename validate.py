from board import COLS

def get_valid_column(board, turn):
    while True:
        try:
            col = input(f"Player {turn + 1}, select a column (0-{COLS - 1}) or type 'exit' to quit: ").strip()
            
            if col.lower() == 'exit':
                print("Exiting the game. Goodbye!")
                exit()

            col = int(col)

            if col < 0 or col >= COLS:
                print(f"Invalid input: Please enter a number between 0 and {COLS - 1}.")
                continue

            if board[0][col] != ' ':
                print("Invalid input: This column is full. Try a different one.")
                continue

            return col
        except ValueError:
            print("Invalid input: Please enter a valid number.")
