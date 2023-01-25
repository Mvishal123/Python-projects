import random

def guess_number(x):
    random_number = random.randint(1, x)
    while(True):
        guess = int(input(f"Guess the number between 1 to {x}: "))
        if guess>random_number:
            print("Sorry, wrong guess. Too high.")
        elif guess<random_number:
            print("Sorry, wrong guess. Too less.")
        else:
            print("Yay! You got it")
            print("")
            again = input("Do you want to play again: ")
            if again == "yes":
                random_number = random.randint(1,x)
            else:
                break


guess_number(10)
