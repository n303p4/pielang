#!/usr/bin/env python3

# stdabPyla
import sys
import pielang
import stdab3

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("> ")
    while 1:
        print(stdab3.decode(pielang.decode(x)))
        x = input("> ")

if __name__ == "__main__":
    main(sys.argv[1::])
