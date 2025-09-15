#!/usr/bin/env python3

n = input()
n = int(n)



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

isneg(n)