import random

print("Guess the Number")
userinput = input("Enter a number between 1 & 100\n")

for x in range(1):
    generatednumber = random.randint(0, 101)

if userinput == generatednumber:
    print("Correct, Number =" + generatednumber)
else:
    print("Incorrect, Correct Number = " + str(generatednumber))
