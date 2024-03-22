"""One Shot Battleship!"""

__author__ = "730643380"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

size_grid: int = 4
secret_row: int = 3
secret_column: int = 2

row_out_of_range: bool = True

guess_row: int = int(input("Guess a row: "))

"""This is explaining that if the guess of the row is out of range then it lets the user know."""

while row_out_of_range:
    if guess_row > size_grid or guess_row < 1:
        guess_row = int(input(f"The grid is only {size_grid} by {size_grid}. Try again: "))
    else:
        row_out_of_range = False

guess_column: int = int(input("Guess a column: "))

"""This is explaining that if the guess of the column is out of range then it lets the user know."""
column_out_of_range: bool = True
while column_out_of_range:
    if guess_column > size_grid or guess_column < 1:
        guess_column = int(input(f"The grid is only {size_grid} by {size_grid}. Try again: "))
    else:
        column_out_of_range = False

"""If the guess is the secret row and column then it will assigns the box to RED BOX, if not, then it will assign it to WHITE BOX."""

if guess_row == secret_row and guess_column == secret_column:
    box = RED_BOX
else: 
    box = WHITE_BOX

"""The code is creating a grid and within the grid it is chekcing each box to see if it is the secret column and row."""  

counter_y: int = 1
while counter_y <= size_grid:
    row = ""
    counter_x = 1
    while counter_x <= size_grid:
        if guess_row == counter_y and guess_column == counter_x:
            row += box
        else:
            row += BLUE_BOX
        counter_x += 1
    print(row)
    counter_y += 1

"""It checks the columns and the rows and gives hints to the user to whether or not the user is close to the secret location."""

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row != secret_row and guess_column == secret_column:
    print("Close! Correct column, wrong row.")
elif guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
else:
    print("Miss!")