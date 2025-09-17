#!/usr/bin/env python3
import sys

def shrink(s: str) -> None:
    print(s[:8])

def enlarge(s: str) -> None:
    print(s + "Z" * (8 - len(s)))

if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("none")
    else:
        for word in args:
            if len(word) > 8:
                shrink(word)
            elif len(word) < 8:
                enlarge(word)
            else:
                print(word)