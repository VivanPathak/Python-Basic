import random
import time

print("""

1. Roll a dice
---------------

2.Exit the program


""")

Random_Number = random.randint(1, 6)
Choice= int(input("Pls enter the no. here:"))

if Choice == 1:
    print("Rolling...")
    time.sleep((2))
    print("[", Random_Number, "]")


elif Choice == 2:
    print("Thanks for using my program",
          " made by - vivan pathak")

else:
    print("You entered a wrong value...")
