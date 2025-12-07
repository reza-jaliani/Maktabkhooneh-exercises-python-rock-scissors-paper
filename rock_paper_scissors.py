#----Import and Global Variables
import random
USER_CHOICES = ["rock","scissors","paper"]


#----Get User Choice
def get_user_input():
    user_choice = input("Your Choice: (rock, scissors, paper)")
    while user_choice not in USER_CHOICES:
        user_choice = input("Your Choice: (rock, scissors, paper)")
    return user_choice

#----Get Computer Chioce
def get_computer_input():
    computer_chioce = random.choice(USER_CHOICES)
    return computer_chioce


#----Determine Winner
def determine_winner(user_choice, computer_choice):
    print("User Choice:" + user_choice)
    print("Computer Choice:" + computer_choice)
    if user_choice == computer_choice:
        print("DRAW!")
    elif (user_choice == "rock" and computer_choice == "scissors") or  (user_choice == "scissors" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "rock"):
        print("User Won")
    else:
        print("Computer Won")

#----Main Function
def main():
    user_selection = get_user_input()
    computer_selection = get_computer_input()
    determine_winner(user_selection,computer_selection)

main()