import random
import time


print("""

welcome to Number Game...
Computer will generate a number from 1 to 100
and you have to guess it  
your have 7 attempts so lets start


""")

Random_Number = random.randint(1,100)
Attempt =  7
Counter  =  1

while True:

    Guess = int(input("Pls enter your guess here: "))

    if Counter > 7 or Attempt < 0:
        print("You used all your attmepts.  Game over")
        break

    elif (Random_Number > Guess):
        print("Comparing Numbers..")
        time.sleep((1))
        print("Your guess is lower than the number.. Try again ")
        Attempt -= 1
        Counter += 1

    elif (Random_Number < Guess):
        print("Comparing Numbers..")
        time.sleep((1))
        print("Your guess is higher than the number..try again ")
        Attempt -= 1
        Counter += 1

    else:
        print("Comparing Number...")
        time.sleep((1))
        print("You guessed it in ", Counter , "attempts(s)")














