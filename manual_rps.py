import random 
choices = ["Rock","Paper", "Scissors"]
def get_user_choice():
    user_input = input("please pick a an option by inputting the number and pressing enter:\n1) rock \n2) paper \n3) scissors\n")
    return choices[int(user_input)-1]
def get_computer_choice():
    return random.choice(choices)
def get_winner(user_choice,computer_choice):
    if user_choice=="Rock":
        if computer_choice=="Rock": 
            print("It's a tie!")
        elif computer_choice=="Paper":
            print("You lost")
        else:
            print("You won!")
    elif user_choice=="Paper":
        if computer_choice=="Rock": 
            print("You won!")
        elif computer_choice=="Paper":
            print("It's a tie!")
        else:
            print("You lost")
    else:
        if computer_choice=="Rock": 
            print("You lost")
        elif computer_choice=="Paper":
             print("You won!")
        else:
            print("It's a tie!")
def play():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"you chose {user_choice}, computer chose {computer_choice}")
    get_winner(user_choice=user_choice,computer_choice=computer_choice)
if __name__=="__main__":
    play()
    
    