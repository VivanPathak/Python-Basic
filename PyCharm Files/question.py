import time
print("""

welcome to Maths Calculator by Vivan Pathak Va
here you can calculate area and perimeter of any of the following shape:
1. Square
2. Rectangle
3. Quit

""")


Operation = int(input(" enter the no. of operation in number   : "))
Length = int(input(" write the length of your shape in number  : "))
Breadth = int(input("write the breadth of your shape in number : "))

if Operation == 1:
    time.sleep((2))
    print("Your shape's area is ",Length*Breadth ,"  and perimeter of your shape is ", Length*4)

elif Operation == 2:
    time.sleep((2))
    print("Your shape's area is ", Length*Breadth, "   and perimeter of your shape is ", (Length+2)+(Breadth+2))

else:
    print("Thanks for using our code thanksss...")

try:
    if Breadth or Length <= 4:
        print("You Have entered a wrong value pls enter the correct value")

except Breadth == str or Length == str:
    print("Enter A correct Value")