String = input("Pls enter

Frequency = dict()

for character in  String:

    if character in Frequency:

        Frequency[character] += 1

    else:

        Frequency[character] = 1

for letter, count in Frequency.items():

     print(letter,":",count)