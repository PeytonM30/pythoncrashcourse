import random

def choose_random():
    return random.randint(0,2)

def check_win(input_1, input_2):
    win_options = ["Tie!", "You Win!", "You Lose!"]
    diff = input_1 - input_2
    return win_options[diff % 3]


def get_user_input():
    valid_input = False
    while not valid_input:
        user_input = input("Rock(0), Paper(1), Scissors(2). (q) to quit: ")
        if user_input == "q":
            return user_input
        elif user_input == "0" or user_input == "1" or user_input == "2" or user_input == "q":
            valid_input = True
            return int(user_input)
        else:
            print("Invalid Input! Try again.")



game_going = True
options = ["Rock", "Paper", "Scissors"]
while game_going:
    user_input = get_user_input()
    if user_input == "q":
        break
    computer_input = choose_random()

    print(f"You chose: {options[user_input]}, Computer chose {options[computer_input]}. ")
    print(check_win(user_input, computer_input))
   #  game_going = False