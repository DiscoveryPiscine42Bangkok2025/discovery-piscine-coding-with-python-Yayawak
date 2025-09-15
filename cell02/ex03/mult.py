#!/usr/bin/env python3

def isneg(n):
    neg = "This number is negative."
    pos = "This number is positive."
    zer = "This number is equal to zero."
    if n > 0:
        print(pos)
    elif n < 0:
        print(neg)
    else:
        print(zer)

try:
    a = int(input("Enter the first number:\n"))
    b = int(input("Enter the second number:\n"))
    c = a * b
    isneg(c)
except ValueError:
    print("One of the inputs is not a valid number.")