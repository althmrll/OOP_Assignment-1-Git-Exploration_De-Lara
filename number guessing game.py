import random
score = 0

#Listing game mechanics
def game_mechanics():
    print ("NUMBER GUESSING GAME\n")
    print ("This is a number guessing game. The game wil choose a number ranging from 1 to 100 and you will have to guess what number the game chose. Don't worry the game will tell you if you guess higher or lower. Good luck!\n")
    print ("----------\n")

#Pressing enter to start
def start_game():
    start=input("Ready to start the game? Press 'ENTER' to start.")
    if start!= "":
        start=input("Press 'ENTER' tot start the game.")
    else: 
        start_game()
        
#Game itself
#Scoring
#Replay (play again/ end game)

game_mechanics()
