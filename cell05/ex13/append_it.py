#!/usr/bin/env python3
import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    for word in args:
        if word.endswith("ism"):
            continue
        print(word + "ism")