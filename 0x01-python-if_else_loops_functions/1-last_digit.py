#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# this nex part it's used to know if the
if number < 0:
    number2 = number * -1
else:
    number2 = number
modulo = number2 % 10
if number < 0:
    modulo = modulo * -1
# modulo is a mathimatical opertator to have the rest of the division
if modulo > 5:
    print("Last digit of", number, "is", modulo, "and is greater than 5")
elif modulo == 0:
    print("Last digit of", number, "is", modulo, "and is 0")
elif modulo < 6 and modulo != 0:
    print("Last digit of", number, "is", modulo, end=" ")
    print("and is less than 6 and not 0")
