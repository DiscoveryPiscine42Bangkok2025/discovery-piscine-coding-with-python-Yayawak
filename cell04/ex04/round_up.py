#!/usr/bin/env python3

import math

a = input("Give me a number: ")

try:
    num = float(a)
    result = math.ceil(num)
    print(result)
except ValueError:
    print("This is not a valid number.")