# Design an algorithm that generates the first n numbers in the following sequence:
# ; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
n = int(input("Enter the length of the sequence: ")) # Do not change this line

sum = 0
num1 = 1
num2 = 2
num3 = 3

for i in range(1, n+1):
    if i == 1:
        print(i)
        continue
    elif i == 2:
        print(i)
        continue
    elif i == 3:
        print(i)
        continue
    sum = (num1 + num2 + num3)
    num1 = num2
    num2 = num3
    num3 = sum
    print(sum)