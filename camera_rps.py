import cv2
from keras.models import load_model
import numpy as np
import time
import random
class Camera_rps():
    """
    A class representing a computer vision based rock paper scissors game.
    ...

    Attributes
    ----------
    default_rounds : int 
            the number of rounds that the user or the computer have to win 
            to conclude the game (default is 3)
    default_countdown : int
            the countdown timer between each rps round in seconds (default is 5) 
    computer_wins : int
            number of wins the computer has scored
    user_wins : int 
            number of wins the user has scored
    model : keras.models
            image recognition model used to predict user choice based on video capture
    data : np.ndarray
            numpy array used to pass in data to the model

    Methods
    -------
    get_prediction(img):
        returns a prediction of "Rock", "Paper" or "Scissors" based on an input image of user playing the game

    update_scores(winner):
        Updates the user and computer scores based on the win condition

    get_computer_choice():
        Returns the randomised computer choice of rock paper or scissors
    
    declare_match_winner():
        declares who won the game based on self.user_wins and self.computer_wins
        
    get_winner(user_choice,computer_choice):
        returns the winner of the rock paper scissors round based on 
        human input and computer choice and traditional rock paper scissors
        rules both printing and returning the winner
    """ 

    def __init__(self, default_rounds:int=3, default_countdown:int=5):
        '''
        Constructs all necessary attributes for the computer vision based rock paper scissors object.

        parameters:
        -----------
        default_rounds: int 
                the number of rounds that the user or the computer have to win 
                to conclude the game (default is 3)
        default_countdown: int
                the countdown timer between each rps round in seconds (default is 5)          
        '''
        self.default_rounds = default_rounds
        self.default_countdown = default_countdown
        self.computer_wins = 0
        self.user_wins = 0
        self.model = load_model('keras_model.h5')
        self.data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    def get_prediction(self,img):
        '''
        returns a prediction of "Rock", "Paper" or "Scissors" based on an input image
            
        Parameters:
        -----------
        img : np.ndarray 
            frame returned from cv2.VideoCapture(0).read() containing the user playing rps
        
        returns:
        -----------
        str
            predicted choice of either "Rock", "Paper", "Scissors" 
            or "Nothing" based on the input the img

        '''

        # 0 Paper
        # 1 Scissors
        # 2 Rock
        # 3 Do-Nothing
        choices = ["Paper","Scissors","Rock","Nothing"]

        resized_frame = cv2.resize(img, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        self.data[0] = normalized_image
        prediction = self.model.predict(self.data) # get model prediction from the resized, normalized frame

        return choices[np.argmax(prediction)] # return the choice based on the highest probability

    def update_scores(self,winner):
        '''
        Updates the user and computer scores based on the win condition

        parameters:
        -----------
        winner : int
            0 = user won, 1 = computer won, 2 = it was tie 

        '''
        if winner ==0:
            self.user_wins+=1
        elif winner ==1:
            self.computer_wins+=1
        else:
            pass

    def get_computer_choice(self):
        '''
        Returns the randomised computer choice of rock paper or scissors
        
        Returns:
        -----------
            str 
                String containing "Rock", "Paper" or "Scissors"
        '''
        choices = ["Rock","Paper", "Scissors"]
        return random.choice(choices)
    
    def declare_match_winner(self):
        '''
        declares who won the game
        '''
        if self.user_wins>self.computer_wins:
            print("Congratulations, you won!! :D")
        else: 
            print("Better luck next time, you lose :(")

    def get_winner(self,user_choice,computer_choice):
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
                print("It's a tie!")
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
                print("It's a tie!")
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
                print("It's a tie!")
                return 2
            
    def play(self):
        '''
        play function to run the whole rps game based on the countdown and rounds set 
        in default_countdown and default_rounds the game ends when either the user 
        or the computer wins the number of rounds set. The default being 3 seconds
        '''

        #Creates a VideoCapture object to capture video from the default camera
        cap = cv2.VideoCapture(0)
        captured=False
        start_time = int(time.time())
        print(f"user score: {self.user_wins}\ncomputer score: {self.computer_wins}")

        while self.user_wins<self.default_rounds and self.computer_wins<self.default_rounds:
            # Capture a frame of video
            ret, frame = cap.read()

            # Check if the frame was successfully captured
            if not ret:
                break

            # Get the current time in seconds since the epoch
            current_time = int(time.time())
            time_delta = start_time-current_time
            # Calculate how many seconds until the next countdown mark
            time_until_0 = time_delta % self.default_countdown

            # Put the remaining time left on the countdown timer
            cv2.putText(frame, str(time_until_0), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Check if it is exactly at the set count down time
            if current_time % self.default_countdown == 0:
                # to avoid multiple captures in the same window due to high frame rate
                if captured==False:
                    # get user choice from frame
                    user_choice = self.get_prediction(frame)
                    print(f"you chose {user_choice}")
                    if user_choice != "Nothing":
                        # get random computer choice
                        computer_choice = self.get_computer_choice()
                        print(f"computer {computer_choice}")
                        # find out who won
                        winner = self.get_winner(user_choice=user_choice,computer_choice=computer_choice)
                        # update scores of the user and computer
                        self.update_scores(winner=winner)
                        print(f"user score: {self.user_wins}\ncomputer score: {self.computer_wins}")
                    else: 
                        print("please try again")
                    captured = True
            else:captured = False
            # Display the modified video with the countdown timer
            cv2.imshow("Frame", frame)

            # Wait for 1 millisecond and check if the 'q' key was pressed
            if cv2.waitKey(1) == ord('q'):
                break
        # print the winner of the match at the end of the game
        self.declare_match_winner()
        # Release the VideoCapture object and close all windows
        cap.release()
        cv2.destroyAllWindows()
        

if __name__ == "__main__":
    rps = Camera_rps()
    rps.play()