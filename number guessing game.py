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
        start=input("Press 'ENTER' to start the game.")
    else: 
        print ("\n----------")
        gameplay()

#Game itself
def gameplay():
    number=random.randint (1,101)
    guess=  0
    print("\nscore:", score,"\n")
    while guess!=number:
        guess = int(input("Enter your guess:"))
        try:
            if guess>number:
                print ("You're thinking too high!!")
                print ("\n----------\n")

            elif guess<number:
                print ("That's too low!")
                print ("\n----------\n")
        
            elif guess==number:
                print ("That's right! The number is", number, "!! You guessed it!")
                scoring ()
                replay  ()
        except ValueError:
            print ("You're silly, you need to guess a number!") or ("You can only type a number silly!")


#Scoring
def scoring():
    score = 0
    score += 1
    print ("Your current score:", score)

#Replay (play again/ end game)
def replay():
    input ("That was fun! Want to play again?")
    if input=="yes" or input=="Yes":
        print ("Great! Here's another round.")
        gameplay()
    
    elif input=="YES":
        print ("Great! Here's another round.")
        gameplay()
    
    elif input=="NO" or input=="no":
        print ("Ok, goodbye :'(")
        exit ()
    
    elif input == "No":
        print ("Ok, goodbye :'(")
        exit ()
    
    else:
        input ("play again?")
        replay_mechanics()
    
game_mechanics()
start_game()

