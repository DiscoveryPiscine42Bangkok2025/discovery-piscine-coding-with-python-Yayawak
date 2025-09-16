#!/usr/bin/env python3

age = input("Please tell me your age: ")
age = int(age)

print(f"You are currently {age} years old.")

a = [10, 20, 30]
for x in a:
    p = f"In {x} years, you'll be {x + age} years old."
    print(p)