from random import randrange
inputFunction = input('Would you like to roll a dice? ')

while inputFunction.lower() == 'y':
    diceNumber = randrange(1, 6)
    print(f'The Dice has been rolled and your number is {diceNumber}!\n')
    inputFunction2 = input('Would you like to reroll?')
    if inputFunction2.lower() == 'n':
        break