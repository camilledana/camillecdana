#Name:Camille Dana
#ID:003277157

print("Enter an integer from 1 to 99:")
attempts = 0
guess = -1

from random import randint
smaller = int(input("Enter a small positive number: "))
larger = int(input("Enter a large positive number: "))

number = randint(smaller,larger)

while number != guess and attempts < 5:
    attempts+=1
    guess = int(input("enter a number: "))

    if guess == number:
        print("You guessed it in ", attempts, "attempts")
    elif attempts == 5:
        print("Game over! Number is",randint)

    elif guess > number:
        print("Guess lower")

    elif guess < number:
        print("Guess higher")


# if guess == winning_number:
# print("You've got it in(guesses+1) tries!")
#
# else:
# guess = int(input("winning_number!"))
# if guess == winning_number:
# print("You've got it in(guesses+2) tries!")
#
# if guess > number:
# print("Guess lower")
#        tries = guesses + 1
#
#     elif guess < number:
#         guess = int(input("Enter a small positive number: "))
#         tries = guesses + 2
#
#     elif guess < number:
#         print("Guess higher")
#         guess = int(input("Enter a large positive number: "))
#        tries = guesses + 3
#
#     elif guess > number:
#         print("Guess lower")
#        tries = guesses + 4
#
#     elif guess > number:
#         print("\nYou've got it in (guesses) "guesses"!)
#         print("You guessed it in ", attempts, "attempts")
# else:
#     while guess == 5:
#         print("Game over! Number is"(number))
#
# input("\n\n Press the enter key to exit")
#
