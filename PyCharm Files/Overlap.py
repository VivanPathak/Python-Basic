O_List = [number for number in range(200) if number % 2 != 0]

P_List = []

for num in range(2,200):
    prime = True

    for i in range(2,num):


        if (num %i == 0):
            prime = False

    if prime:
        P_List.append(num)

with open("Odd_Numbers.txt","w") as Odd_Numbers:

    for numbers in O_List:
        Odd_Numbers.write(str(numbers)+ ", ")

with open("Prime_Numbers.txt","w") as Prime_Numbers:

    for numbers in P_List:
        Prime_Numbers.write(str(numbers)+", ")

Overlap = []

for numbers in P_List:

    if numbers in O_List:
        Overlap.append(numbers)

with open ("Overlap_Numbers.txt","w") as Overlap_Numbers:
    for numbers in Overlap:
        Overlap_Numbers.write(str(numbers)+", ")