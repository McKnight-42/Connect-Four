# Connect-Four
Connect Four is a classic two-player board game implemented in Python. The objective of the game is to be the first to connect four of your pieces in a row, either horizontally, vertically, or diagonally.

# Features
Two-player mode: Play against a friend on the same computer.
Single-player mode: Play against a computer opponent.
Smart AI: The computer player tries to block your winning moves and select optimal moves.
Game state display: A visual representation of the game board that updates after each move.
Replay option: After a game finishes, you can choose to play again.
Input validation: Ensures that players input valid columns and prevents invalid moves.
Prerequisites
To run the game locally, you need to have Python installed. This project has been tested with Python 3.x.

You can download and install Python from the official Python website.

# Installation
Clone this repository to your local machine:

```
git clone https://github.com/McKnight-42/Connect-Four.git
```

Navigate to the project directory:

```
cd Connect-Four
```

(Optional) Create a virtual environment for managing 

```
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```


# How to Play

## Run the Game:

To start the game, run the following command:

```
python main.py
Gameplay Instructions:
```

The board has 6 rows and 7 columns.
Players take turns to drop their pieces (🔴 for Player 1, 🟡 for Player 2) into one of the columns.
The piece will fall to the lowest available row in that column.
The first player to connect four pieces in a row, column, or diagonal wins the game.
Choosing the Game Mode:

At the start of the game, you can choose to play two-player or single-player against the computer.
In single-player mode, the computer will make moves automatically and try to block your winning moves.
Replay Option:

After each game, you will be asked if you'd like to play again.
Game Logic
The game is implemented using simple game logic:

Board Representation: The game board is a 6x7 grid.
Winning Conditions: The game checks for horizontal, vertical, and diagonal connections of four pieces of the same player.
AI Move Selection: The computer uses a simple strategy to block the human player's winning moves and chooses a random move when no blocking is needed.

# Running Tests

You can run the tests by executing the following command in the terminal:
```
python -m unittest test.py

```

# Files

board.py: Contains functions related to the board, such as creating and printing the board.
check_win.py: Contains the logic to check for a winner or a tie.
game.py: Contains the main game logic.
main.py: The entry point of the program that starts the game.
validate.py: Handles input validation and move checks.
test.py: Contains unit tests for game logic (you can run these tests to check the correctness of the game).
