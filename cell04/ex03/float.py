#!/usr/bin/env python3

a = input("Give me a number: ")

x = "This number is an integer."
y = "This number is a decimal."

try:
    int_val = int(a)
    print(x)
except ValueError:
    try:
        float_val = float(a)
        print(y)
    except ValueError:
        print("This is not a number.")