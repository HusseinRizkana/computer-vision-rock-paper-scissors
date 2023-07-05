import random 


def get_user_choice():
    '''
    get user choice by inputing 1, 2 or 3 (fixes issues with user spelling errors)
    returns:
    -----------
    str
        either "Rock", "Paper", "Scissors" 
    '''
    choices = ["Rock","Paper", "Scissors"]
    user_input = input("please input your choice from Rock, Paper, Scissors")
    assert(user_input.lower().capitalize() in choices)
    return user_input


def get_computer_choice():
    '''
    get computer randomly assigned choice
    returns:
    -----------
    str
        either "Rock", "Paper", "Scissors" 
    '''
    choices = ["Rock", "Paper", "Scissors"]

    return random.choice(choices)


def get_winner(computer_choice,user_choice):
    '''
    returns the winner of the rock paper scissors round based on 
    human input and computer choice and traditional rock paper scissors
    rules
    both printing and returning the winner
    
    parameters: 
    -----------
        user_choice : str 
            users choice of "Rock", "Paper" or "Scissors"
        computer_choice : str 
            computers choice of "Rock", "Paper", or "Scissors"

    returns:
    -----------
        int
            0 = user won, 1 = computer won, 2 = it was tie  


    '''
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
    '''
    runs one round of the manual rock paper scissors terminal game
    '''
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"you chose {user_choice}, computer chose {computer_choice}")
    get_winner(user_choice=user_choice,computer_choice=computer_choice)


if __name__=="__main__":
    play()
    
    