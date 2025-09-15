#!/usr/bin/env python3

n = (int)(input("Enter a number less than 25\n"))

if (n > 25):
    print("Error")
    exit()


for i in range(n, 26):
    print("Inside the loop, my variable is ", i)