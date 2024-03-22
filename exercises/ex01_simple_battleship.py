"""EX01 - Simple Battleship - A cute step toward Battleship."""
 
__author__ = "730643380"

BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

P1: int = int(input("Pick a secret boat location between 1 and 4: "))

if P1 < 1:
    print(f"Error! {P1} too low!")
    exit()
elif P1 > 4:
    print(f"Error! {P1} too high!")
    exit()

P2: int = int(input("Guess a number between 1 and 4: "))

if P2 < 1:
    print(f"Error! {P2} too low!")
    exit()
elif P2 > 4:
    print(f"Error! {P2} too high!")
    exit()

box: str = ""

if P2 == P1:
    box = RED_BOX
else: 
    box = WHITE_BOX

finalout: str = ""

if P2 == 1:
    finalout += box
else:
    finalout += BLUE_BOX

if P2 == 2:
    finalout += box
else:
    finalout += BLUE_BOX

if P2 == 3:
    finalout += box
else:
    finalout += BLUE_BOX

if P2 == 4:
    finalout += box
else:
    finalout += BLUE_BOX

print(finalout)

if P2 == P1:
    print("Correct! You hit the ship.")
    
else: 
    print("Incorrect! You missed the ship.")