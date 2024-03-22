"""Number Guessing Game."""
from random import randint

SECRET: int = randint(1,1000)
correct: bool = False

while correct == False:
    guess: int = int(input("Guess a number: "))
    if guess==SECRET:
        correct=True
    elif guess < SECRET:
        print("Too low")
    else:
        print("Too high")

print("You win!!!")



