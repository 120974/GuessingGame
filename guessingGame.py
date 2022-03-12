import random

number = random.randrange(1, 50)

chanceCount=0

print("Number guessing game")
print("Guess a number (between 1 and 50)")
print("You have 5 chances.")

while chanceCount < 10:
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