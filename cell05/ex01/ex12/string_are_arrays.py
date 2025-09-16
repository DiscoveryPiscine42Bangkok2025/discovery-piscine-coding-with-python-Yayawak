#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if len(args) != 1:
    print("none")
else:
    s = args[0]
    found = False
    for ch in s:
        if ch == "z":
            print("z", end="")
            found = True
    if not found:
        print("none")
    else:
        print()  