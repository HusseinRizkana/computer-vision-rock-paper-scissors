# Rock-Paper-Scissors-Repo
> This is a rockpaper scissors game to be played using computer vision. The tools used are teachablemachines was used
for creating the model to detect rock paper and scissors with the output being a tensorflow keras model.

## Milestone 1

- Teachable machines was used for creating the computer vision model that detects rock paper and scissors hand gestures
this will be used in the continuation of this project in creating the full game

## Milestone 2 
- Logic was written for basic rock paper scissors following the conventional game rules for a user to play against the computer as a command line game.

The code has 4 functions: 
 1. Getting the choices
```
get_user_choice():
```
the get_usuer_choice() function prompts the user in the command line to choose one of the 3 options by inputting 1, 2 or 3:

```
please pick a an option by inputting the number and pressing enter:
1) rock 
2) paper 
3) scissors
```
the user can then input their choice of action from the choices of 1,2 or 3.
```
get_computer_choice()
```
The get_computer_choice() function uses the random.choice() function from the random module to randomly choose an option to play as the computer choice.

2. Game logic
```
get_winner()
```
The get_winner() function contains the logic for the traditional rock paper scissors game retrieving 2 inputs strings of "Rock", "Paper" or "Scissors" and comparing them and printing the result of win, lose or tie.

3. Wrapping the game
```
play()
```

the play function wraps the functionality of the game so that choice retrieval and game logic are in one pipeline where the user can input their choice and find out how they have done against the computer. 
```
please pick a an option by inputting the number and pressing enter:
1) rock 
2) paper 
3) scissors
1
you chose Rock, computer chose Rock
It's a tie!
```
