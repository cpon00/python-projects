import random


def guess(number):
    correct_guess = False
    while not correct_guess:
        answer = int(input("Guess a number: "))
        if answer == number:
            print("You got it! The number was " + str(number))
            correct_guess = True
        elif answer > number:
            print("Too high! Aim lower...")
            continue
        elif answer < number:
            print("Too low! Raise your expectations!")
            continue


guess(random.randint(0, 25))

