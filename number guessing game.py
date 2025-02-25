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
        gameplay()

#Game itself
def gameplay():
    number=random.randint (1,101)
    guess=  0
    print("score: {score}")
    guess = int(input("Enter your guess:"))
    try:
        if guess>number:
            print ("You're thinking too high!") or ("Not quite, think lower!")

        elif guess<number:
            print ("That's too low!") or ("Nope, think bigger!")
        
        else:
            print ("That's right! The number is {number}! You guessed it!")
            scoring ()
            replay  ()

    except ValueError:
        print ("You're silly, you need to guess a number!") or ("You can only type a number silly!")


#Scoring
def scoring():
    score += 1
    print ("Your current score: {score}")

#Replay (play again/ end game)
def replay():
    r = input ("That was fun! Want to play again?")
    replay_mechanics()

def replay_mechanics():
    if r == "yes" or r == "Yes":
        print ("Great! Here's another round.")
        gameplay()
    
    elif r == "YES":
        print ("Great! Here's another round.")
        gameplay()
    
    elif r == "NO" or r == "no":
        print ("Ok, goodbye :'(")
        exit ()
    
    elif r == "No":
        print ("Ok, goodbye :'(")
        exit ()
    
    else:
        r = input ("play again?")
        replay_mechanics()
    
game_mechanics()
start_game()

