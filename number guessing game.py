import random
round = 1
score = 0

#Listing game mechanics
def game_mechanics():
    print ("NUMBER GUESSING GAME\n")
    print ("This is a number guessing game. The game wil choose a number ranging from 1 to 100 and you will have to guess what number the game chose. Don't worry the game will tell you if you guess higher or lower. Good luck!\n")
    print ("----------\n")

#Pressing enter to start
def start_game():
    start=input("Ready to start the game? Press 'ENTER' to start.")
    while True:
        if start == "":
            print ("\n----------")
            gameplay()
        else: 
            start=input("Press 'ENTER' to start the game.")

#Game itself
def gameplay():
    number=random.randint (1,100)
    print ("\nROUND", round, ":\n\n")
    guess=  0
    print("\nscore:", score,"\n")

    while guess!=number:
        try:
            guess = int(input("Enter your guess:"))
            if guess>number:
                print ("You're thinking too high!!")
                print ("\n----------\n")

            elif guess<number:
                print ("That's too low!")
                print ("\n----------\n")
                
            else:
                print ("\n----------")
                print ("\nThat's right! The number is", number, "!! You guessed it!\n")
                scoring ()
                replay  ()

        except ValueError:
            print ("You can only type a number silly!\n")
            print ("----------\n")
    
#Scoring & Round
def scoring():
    global score
    global round
    score= score + 1
    round = round + 1
    print ("Your current score:", score, "\n")

#Replay (play again/ end game)
def replay():
        rp = input ("That was fun! Want to play again? (y/n):")
        while True:
            if rp=="y" or rp=="Y":
                print ("Great! Here's another round.\n")
                print ("\n----------\n")
                gameplay()
    
            elif rp=="N" or rp=="n":
                print ("Ok, goodbye :'(")
                exit ()
                
            else:
                rp= input("play again?(y/n):")
             
game_mechanics()
start_game()
