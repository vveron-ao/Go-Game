# Go! Game

This code implements a simple game where two players take turns placing "stones" (represented by different characters) on a 9x9 board, which is displayed as a grid. The players input coordinates, and the game updates the board after each valid move. Below is a breakdown of its functionality:
Board Initialization:
The board is represented as a list of lists (row), where each element is initially ' . ' to indicate an empty space.
The variable blackChar holds the symbol for Black's stone (an open circle, ◯), and whiteChar holds the symbol for White's stone (a solid circle, ●).

Board Display:
The game begins by printing instructions for input format and displaying the initial empty board. Each row is printed with numbers along the left, and the columns are numbered at the bottom.

Game Loop:
The game runs in a loop, alternating between Black and White turns. Each player enters their move by specifying an X and Y coordinate (e.g., 12 for X=1, Y=2).
The code checks the validity of the player's input, ensuring it is in the correct format and within the board's boundaries.
If the chosen position on the board is empty (' . '), the corresponding spot is updated with either Black's or White's stone symbol.
The board is reprinted after each valid move to reflect the updated state.

Stopping the Game:
Players can type 'stop' at any time to exit the game.

Turn Tracking:
The variable evenOdd determines whose turn it is. Black goes on even turns, and White goes on odd turns.
The code ensures players can't place stones on already occupied positions, and invalid inputs prompt the player to try again without changing the board.
