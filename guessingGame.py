import random

number = random.randrange(1, 9)

chanceCount=0

print("Print a number between 1 and 9")
print("you have 5 chances. Good Luck.")

while chanceCount < 5:
    guess = int(input("Enter your guess: "))
    chanceCount = chanceCount + 1

    if guess < number:
        print("Too low! Guess a number higher than ", guess)
        
    if guess > number:
        print("Too high! Guess a number lower than ", guess)

    if guess == number:
        print("You win!!")
        break

    if not chanceCount < 5:
        print("You lose! The number is ", number)