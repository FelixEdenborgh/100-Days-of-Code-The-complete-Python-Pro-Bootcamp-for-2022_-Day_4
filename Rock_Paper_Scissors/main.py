import random


print("Welcome to this Rock Paper and Sissor game! \nCan you win over the bot? or are you a noob. \nLets see!")
play = True
while(play == True):
    userInput = input("What Do you Choice: Rock = 0, Paper = 1, Sissor = 2, or any number to end the game \n:")
    bot = str(random.randint(0,2))

    if(userInput == "0" and bot == "2"):
        print("You have Won!")

    elif (userInput == "2" and bot == "0"):
        print("Bot have won!")

    elif(userInput == "1" and bot == "0"):
        print("You have Won!")

    elif(userInput == "0" and bot == "1"):
        print("Bot have won!")

    elif(userInput == "2" and bot == "1"):
        print("You have Won!")

    elif(userInput == "1" and bot == "2"):
        print("Bot have won!")


    elif(userInput == "0" and bot == "0"):
        print("No one won both lose!")

    elif (userInput == "1" and bot == "1"):
        print("No one won both lose!")

    elif (userInput == "2" and bot == "2"):
        print("No one won both lose!")

    elif(userInput != "1" or userInput != "2" or userInput != "3"):
        print("Game ending")
        play = False
