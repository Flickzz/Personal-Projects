for i in range (1,21):
    if (i == 4 or i == 13):
        state = "UNLUCKO"
    elif(i%2 == 0):
        state = "EVEN"
    else:
        state = "ODD"
    print(f"{i} is {state}")