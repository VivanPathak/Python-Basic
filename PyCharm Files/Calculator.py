import math

print("""

1. Addition
2. Subtraction
3. Multiplication
4. Division 
5. Quit

""")

Operation = int(input("Please enter the no. of the operation you wanna do: "))

if Operation == 1:
    Number_1 = int(input("Pls enter a value: "))
    Number_2 = int(input("Pls enter the second value: "))

    print("Result:  ", Number_1 + Number_2)

elif Operation == 2:
    Number_1 = int(input("Pls enter a value: "))
    Number_2 = int(input("Pls enter the second value: "))

    print("Result:  ", Number_1 - Number_2)

elif Operation == 3:
    Number_1 = int(input("Pls enter a value: "))
    Number_2 = int(input("Pls enter the second value: "))

    print("Result:  ", Number_1 * Number_2)

elif Operation == 4:
    Number_1 = int(input("Pls enter a value: "))
    Number_2 = int(input("Pls enter the second value: "))

else:
    print("Thanks for using the calculator")









