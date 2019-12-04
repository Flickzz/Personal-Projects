winningScores = [0, 1, 2, 3, 4, 5]

scoreOfApple = 3*winningScores[0] + 2*winningScores[1] + winningScores[2]
scoreOfBannana = 3*winningScores[3] + 2*winningScores[4] + winningScores[5]

if scoreOfApple > scoreOfBannana:
    print('The Apple team wins!')
elif scoreOfBannana > scoreOfApple:
    print('The Bannana team wins!')
else:
    print('Tie!!!')
print(scoreOfApple)
print(scoreOfBannana)