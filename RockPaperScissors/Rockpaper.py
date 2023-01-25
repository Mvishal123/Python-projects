import random
print('''                        WELCOME TO ROCK PAPER AND SCISSOR GAME''')
choices = ["rock", "paper", "scissor"]
while True:
    player_choice = input("Enter your choice(rock, paper, scissor or leave): ")
    player_choice = player_choice.lower()
    if player_choice == "leave":
        print("Thanks for playing")
        break
    if player_choice not in choices:
        print("Your choice is Invalid :(")
        continue
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print("It's a TIE")
    elif player_choice == "rock" and computer_choice == "scissor":
        print("You WIN!!")
    elif player_choice == "paper" and computer_choice == "rock":
        print("Hurray!! You WIN")
    elif player_choice == "scissor" and computer_choice == "paper":
        print("Its time to party!!")
    else:
        print("hahaha LOSER")