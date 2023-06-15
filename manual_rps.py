import random 
def get_user_choice_numerical():
    choices = ["Rock","Paper", "Scissors"]

    user_input = input("please pick a an option by inputting the number and pressing enter:\n1) rock \n2) paper \n3) scissors\n")
    return choices[int(user_input)-1]
def get_user_choice():
    choices = ["Rock","Paper", "Scissors"]
    return input("please input your choice from Rock, Paper, Scissors")
def get_computer_choice():
    choices = ["Rock", "Paper", "Scissors"]

    return random.choice(choices)
def get_winner(computer_choice,user_choice):
    # 0 is a user win, 1 is a computer win, 2 is a tie
    if user_choice=="Rock":
        if computer_choice=="Rock": 
            print("It is a tie!")
            return 2
        elif computer_choice=="Paper":
            print("You lost")
            return 1
        else:
            print("You won!")
            return 0
    elif user_choice=="Paper":
        if computer_choice=="Rock": 
            print("You won!")
            return 0
        elif computer_choice=="Paper":
            print("It is a tie!")
            return 2
        else:
            print("You lost")
            return 1
    else:
        if computer_choice=="Rock": 
            print("You lost")
            return 1
        elif computer_choice=="Paper":
             print("You won!")
             return 0
        else:
            print("It is a tie!")
            return 2
def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"you chose {user_choice}, computer chose {computer_choice}")
    get_winner(user_choice=user_choice,computer_choice=computer_choice)
if __name__=="__main__":
    play()
    
    