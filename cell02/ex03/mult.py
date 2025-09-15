#!/usr/bin/env python3


a = input("Enter the first number:\n")
b = input("Enter the second number:\n")
a = (int)(a)
b = (int)(b)

c = a * b


def isneg(n):
    neg = "This number is negative."
    pos = "This number is positive."
    zer = "This number is both positive and negative."
    if n > 0:
        print(pos)
    elif n < 0: 
        print(neg)
    else:
        print(zer)
    
isneg(c)