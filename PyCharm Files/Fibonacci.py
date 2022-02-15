
Number_1 = 1
Number_2 = 2

Fibonacci = []


for value in range(15):
    Number_1, Number_2 = Number_2, Number_1 + Number_2
    Fibonacci.append(Number_2)

print(Fibonacci)
