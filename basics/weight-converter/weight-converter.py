import math

multiplier = 2.2

weight = int(input("Weight: ").upper())

typeOfWeight = input("(L)bs or (K)g: ").upper()

if typeOfWeight == 'L':
    resultWeight = weight // multiplier
    print(f"Your weight in kilos is {round(resultWeight, 2)}")
elif typeOfWeight == 'K':
    resultWeight = weight * multiplier
    print(f"Your weight in pounds is {round(resultWeight, 2)}")
else:
    print("Wrong unit.")

