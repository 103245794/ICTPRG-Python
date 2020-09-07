# Program to build a game that a user guesses a random number between 1 and 25
# Linked to Github repository

# importing the random module
import random

# generate a random number between 1 and 25
randomNumber = random.randint(1, 25)

# define variable and an array
attempt = 1
number = 0
remainder = 0
guessList = []

print("Hey there! Lets play a little guessing game.")
print("Guess the number between 0 and 25")

# repeat until 7 attempts
while (attempt <= 7):
    remainder = 7 - attempt

# allow the user to input a guess
    number = int(input("Enter Guess: "))
    guessList.append(int(number))

# when the guess equals the random number
    if (randomNumber == number):
        print("Damn. You win!")
        print("The number was indeed " + str(randomNumber))
        print("You guessed in " + str(attempt) + " guesses")
        break

# when then guess is greater than the random number
    elif (randomNumber < number):
        print("Nope, its less than that")

# when then guess is less than the random number
    else:
        print("Nope, its greater than that")
    print("You have " + str(remainder) + " guesses left!")
    attempt = attempt + 1

# when there's no more attempts remaining
    if (remainder == 0):
        print("AHHAHA YOU LOOSE!")
        print("The number was " + str(randomNumber) + " you fool.")

# print the numbers user entered
print("Your guess log:")
print(guessList)