import random

choices = ('r','p','s')

while True:
    
    
    user_choice = input("Rock, Paper, Scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print('Invalid Choice!')
        continue

    computer_choice = random.choice(choices)
    
    if user_choice == "r":
        print("You chose: Rock")
    elif user_choice == "p":
        print("You chose: Paper")
    else:
        print("You chose: Scissors")

    if computer_choice == "r":
        print("Computer chose: Rock")
    elif computer_choice == "p":
        print("Computer chose: Paper")
    else:
        print("Computer chose: Scissors")


    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "r" and computer_choice == "s":
        print("You won!")
    elif user_choice == "p" and computer_choice == "r":
        print("You won!")
    elif user_choice == "s" and computer_choice == "p":
        print("You won!")
    else:
        print("You lose!")
    
    should_continue = input("Do You Want To Continue? (y/n): ").lower()
    if should_continue == "n":
        break


    

