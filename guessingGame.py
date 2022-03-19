import random
from tkinter import UNDERLINE

number = random.randrange(1, 50)

chanceCount=0

class color:
    RED = '\033[91m'
    BOLD ='\033[1m'
    END ='\033[0m'
    UNDERLINE = '\033[4m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'


print(color.GREEN +"---------------------------------")
print(color.RED + color.BOLD + color.UNDERLINE +"Number guessing game" + color.END)
print(color.GREEN +"---------------------------------")
print(color.YELLOW +"Guess a number (between 1 and 50)")
print("You have 5 chances.")
print(color.GREEN + "---------------------------------")

while chanceCount < 10:
    guess = int(input(color.END + "Enter your guess: "))
    chanceCount = chanceCount + 1

    if guess < number:
        print("Too low! Guess a number higher than", guess)
        print(color.GREEN +"---------------------------------")
        
    if guess > number:
        print("Too high! Guess a number lower than", guess)
        print(color.GREEN +"---------------------------------")

    if guess == number:
        print("You win!!")
        break

    if not chanceCount < 10:
        print("You lose! The number is ", number)
