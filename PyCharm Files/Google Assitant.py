import random
import time
Name = input("What Can I Call You: ")
Surname = input("Wht is your last name: ")
Age = int(input("Enter Your Age here: "))
DOB = input("Enter Your Birth Date And Year: ")
Location = input("Enter Your Location Here: ")
Gender = input("Pls enter your gender here like:- Boy Or Girl: ")
print("""Wait For  A minute.....  Your Information is secure in our hands... """)
time.sleep((3))

print("Hi,", Name, ".Your Assistant Here. There's a lot I can help you with :- """"


1. Play A Game
2. About Me
3. Quit

""")

Operation = int(input("Please enter the no. of the operation you wanna do: "))

if Operation == 1:
    print("""

    welcome to Number Game...
    Computer will generate a number from 1 to 100
    and you have to guess it  
    your have 7 attempts so lets start


    """)

    Random_Number = random.randint(1, 100)
    Attempt  = 7
    Counter = 1

while True:

    Guess = int(input("Pls enter your guess here: "))

    if Counter > 7 or Attempt < 0:
            print("You used all your attmepts.  Game over")
            break

    elif Random_Number > Guess:
            print("Comparing Numbers..")
            time.sleep((1))
            print("Your guess is lower than the number.. Try again ")
            Attempt -= 1
            Counter += 1

    elif Random_Number < Guess:
            print("Comparing Numbers..")
            time.sleep((1))
            print("Your guess is higher than the number..try again ")
            Attempt -= 1
            Counter += 1

    else:
            print("Comparing Number...")
            time.sleep((1))
            print("You guessed it in ", Counter, "attempts(s)","Thanks for playing ,hey assitant where are you???")
            time.sleep((3))
            break

print("I am here ,Number game ,thanks for coming bye.. ok whatever","Hi,", Name, " Your assitant here for you again.  There's a lot I can help you with :- """"


1. Play A Game
2. About Me
3. Quit

""")

Operation = int(input("Please enter the no. of the operation you wanna do: "))

if Operation == 2:
    print(Name,Surname,"is a really intelligent, good looking, Obedient and a respectful",Gender,Name,"Is",Age,"Years old.",Name,"Which lives in ",Location,"and He is a member of our #AssitantTeam as he uses this amazing")