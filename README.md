# Rock-Paper-Scissors-Repo
> This is a rockpaper scissors game to be played using computer vision. The tools used are teachablemachines was used
for creating the model to detect rock paper and scissors with the output being a tensorflow keras model.

## Milestone 1

- Teachable machines was used for creating the computer vision model that detects rock paper and scissors hand gestures
this will be used in the continuation of this project in creating the full game
### Training the model
- A model was trained using https://teachablemachine.withgoogle.com/ to predict user input of Rock, Paper or Scissors using their conventional hand signs.
- After training the model was extracted as a keras model and used for predicting user input

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

## Milestone 3 
- The game was adapted to use computer vision instead of the terminal for the user input of rock paper or scissors and encapsulated in a Camera_rps() class
- This update allows the user to play against the computer using their camera. The first to 3 wins wins.

### How to play the game
1. clone the github repo by running in the terminal
```
git clone https://github.com/HusseinRizkana/computer-vision-rock-paper-scissors.git
```
2. install the dependencies
```
pip install -r requirements.txt
```
3. run the game file to start the game 
```
python main.py
```
4. Starting the game shows the video stream from the users camera with a countdown timer starting the game and countdown timer.
![Alt text](assets/demoVideo.gif)
> The gif above shows an example of how you would play the game
5. once the countdown reaches 0 your input will be put to the test against the generated rock paper scissors choice of the computer. 
6. The game repeats until you are or the computer reach the set number of wins to win the game (default = 3 wins)



### Game Settings
- Changing maximum number of wins:

    to edit the maximum number of wins to win the game,  the Camera_rps() class attribute  default_rounds can be editted in the main.py file class constructor to however many wins the user would like to play to. 
    ```
    if __name__ == "__main__":
        rps = Camera_rps(default_rounds=5)
        rps.play()
    ```
- Changing countdown timer length: 

    to edit the countdown timer length to player response capture, the Camera_rps() class attribute default_countdown can be editted in the main.py file class constructor to however long the user would like the countdown to be in seconds. 

    ```
    if __name__ == "__main__":
        rps = Camera_rps(default_countdown=10)
        rps.play()
    ```
