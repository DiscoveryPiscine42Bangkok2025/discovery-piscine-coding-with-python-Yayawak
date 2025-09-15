#!/usr/bin/env python3

n = input()
n = int(n)


def iszero(n):
    warn = "This number is equal to zero."
    ok = "This number is different from zero."

    s = ok
    if n == 0:
        s = warn

    print(s)
    
iszero(n)