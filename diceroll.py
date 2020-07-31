import random

#variables
#generates random dice number 1-6
playerRoll = random.randint(0,6)
computerRoll = random.randint(0,6)
#variables to check against user input
lowerYes = "y"
upperYes = "Y"
lowerNo = "n"
upperNo = "N"
#Create loop to keep playing
while True:
    #check if user want to keep playing
    readyCheck = input("Ready to roll? Y/N")
    if readyCheck == lowerNo:
        print("Maybe next time")
        break
    elif readyCheck == upperNo:
        print("Maybe next time")
        break 
    elif readyCheck == lowerYes:
        print("Let's get started! You rolled a " + str(playerRoll) + "." + " I rolled a " + str(computerRoll) + ".")
    elif upperYes in readyCheck:
        print("Let's get started! You rolled a " + str(playerRoll) + "." + " I rolled a " + str(computerRoll) + ".")
        #game logic
        if playerRoll > computerRoll:
            print("You win!")
        elif playerRoll == computerRoll:
            print("It's a Tie!")
        else:
            print("I won!")



