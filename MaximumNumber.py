# store the first number in a variable,
# if the next number is larger, then store that number
# print the number when the input is negative


numberInput = int(input())
numberStored = 0
while numberInput > 0:
    if numberInput > numberStored:
        numberStored = numberInput

    numberInput = int(input())
print(numberStored)
