#from getpass import getpass as input
print("E P I C    🥌  📄 ✂️    B A T T LE")
print()
exit = False
playerOneScore = 0
playerTwoScore = 0
while(exit != True):
    firstPlayer = input("Player one, select your move (R, P or S): ")
    secondPlayer = input("Player two, select your move (R, P or S): ")
    if firstPlayer == "R":
      if secondPlayer == "R":
        print("It's a tie!")
      elif secondPlayer == "P":
        print("Player two wins!")
        playerTwoScore += 1
      elif secondPlayer == "S":
        print("Player one wins!")
        playerOneScore += 1
      else:
        print("Invalid move, player two!")
    elif firstPlayer == "P":
      if secondPlayer == "R":
        print("Player one wins!")
        playerOneScore += 1
      elif secondPlayer == "P":
        print("It's a tie!")
      elif secondPlayer == "S":
        print("Player two wins!")
        playerTwoScore += 1
      else:
        print("Invalid move, player two!")
    elif firstPlayer == "S":
      if secondPlayer == "R":
        print("Player two wins!")
        playerTwoScore += 1
      elif secondPlayer == "P":
        print("Player one wins!")
        playerOneScore += 1
      elif secondPlayer == "S":
        print("It's a tie!")
      else:
        print("Invalid move, player two!")
    else:
      print("Invalid move, player one!")
    print("Player 1 Score: ",playerOneScore)
    print("Player 2 Score: ",playerTwoScore)
    decision = input("Do you want continue playing?: ")

    if(decision == "yes" or decision == "YES" or decision == "Yes"):
      exit = False
    else:
      print("GAME OVER!!")
      print("Player 1: ",playerOneScore, "Player 2: ",playerTwoScore)
      if playerOneScore > playerTwoScore:
        print("Player 1 win!!")
      elif playerTwoScore > playerOneScore :
        print("Player 2 win!!")
      else :
        print("It was a draw")
      exit = True