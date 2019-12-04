import random
randomNum = random.randint(1, 10)

userGuess = False
userInput = int(input("Guess a number between 1 and 10: "))
while(userGuess == False):
    if(userInput == randomNum):
        print("NICE 1!! YOU GOT THE NUMBER")
        userGuess = True
        break
    elif userInput < randomNum:
        print("Oooh, your number is less than our current number")
    elif userInput > randomNum:
        print("Oooh, your number is greater than our current number")
    userInput = int(input("Guess Again: "))
