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

user_input = input()

try:
    n = int(user_input)
    isneg(n)
except ValueError:
    print("This is not a number.")