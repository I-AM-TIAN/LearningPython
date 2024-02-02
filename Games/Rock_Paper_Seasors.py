from getpass import getpass as input
print("E P I C    🥌  📄 ✂️    B A T T LE")
print()
firstPlayer = input("Player one, select your move (R, P or S): ")
secondPlayer = input("Player two, select your move (R, P or S): ")
if firstPlayer == "R":
  if secondPlayer == "R":
    print("It's a tie!")
  elif secondPlayer == "P":
    print("Player two wins!")
  elif secondPlayer == "S":
    print("Player one wins!")
  else:
    print("Invalid move, player two!")
elif firstPlayer == "P":
  if secondPlayer == "R":
    print("Player one wins!")
  elif secondPlayer == "P":
    print("It's a tie!")
  elif secondPlayer == "S":
    print("Player two wins!")
  else:
    print("Invalid move, player two!")
elif firstPlayer == "S":
  if secondPlayer == "R":
    print("Player two wins!")
  elif secondPlayer == "P":
    print("Player one wins!")
  elif secondPlayer == "S":
    print("It's a tie!")
  else:
    print("Invalid move, player two!")
else:
  print("Invalid move, player one!")
