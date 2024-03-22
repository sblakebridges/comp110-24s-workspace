"""EX03 - Functional Battleship!"""

__author__ = "730643380"

import random

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def input_guess(size: int, specify: str) -> int:
    """This function is working with the guess of the user. If you guess a row or column outside the range then it will let you know. Specify is used to plug in row or column."""
    assert specify == "row" or specify == "column"
    out_of_range: bool = True
    guess: int = int(input(f"Guess a {specify}: "))
    while out_of_range:
        if guess > size or guess < 1:
            guess = int(input(f"The grid is only {size} by {size}. Try again: "))
        else:
            out_of_range = False
    return guess


def print_grid(size: int, guess_row: int, guess_column: int, guess_user: bool) -> None:
    """This function is using a while loop to display the grid of the battleship."""
    counter_y: int = 1
    if guess_user:
        box = RED_BOX
    else: 
        box = WHITE_BOX
    while counter_y <= size:
        row = ""
        counter_x = 1
        while counter_x <= size:
            if guess_row == counter_y and guess_column == counter_x:
                row += box
            else:
                row += BLUE_BOX
            counter_x += 1
        print(row)
        counter_y += 1


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """This function shows that if you get the guess right then it is true, otherwise it is false."""
    return guess_row == secret_row and guess_column == secret_column


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """Main is a game loop, that makes the usr guess and row and column and lets them know if they get it right or wrong."""
    turns: int = 1
    correct: bool = False
    while (turns <= 5 and not correct):
        print(f"=== Turn {turns}/5 ===")
        guess_row: int = input_guess(grid_size, "row")
        guess_column: int = input_guess(grid_size, "column")
        correct = correct_guess(secret_row, secret_column, guess_row, guess_column)
        print_grid(grid_size, guess_row, guess_column, correct)
        if not correct:
            print("Miss!")
        turns += 1
    if correct:
        print(f"Hit! \n You won in {turns - 1}/5 turns!")
    else:
        print("X/5 - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))