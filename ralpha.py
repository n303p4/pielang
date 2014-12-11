#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Reverse alphabet cipher"

import sys, re

table0 = {"a": "z",
          "b": "y",
          "c": "x",
          "d": "w",
          "e": "v",
          "f": "u",
          "g": "t",
          "h": "s",
          "i": "r",
          "j": "q",
          "k": "p",
          "l": "o",
          "m": "n",
          "n": "m",
          "o": "l",
          "p": "k",
          "q": "j",
          "r": "i",
          "s": "h",
          "t": "g",
          "u": "f",
          "v": "e",
          "w": "d",
          "x": "c",
          "y": "b",
          "z": "a"}

def decode(string, translate=False, html_mode=False):
    array = []
    for character in string:
        if character in table0.keys():
            array.append(table0[character])
        elif character.lower() in table0.keys():
            array.append(table0[character.lower()].upper())
        else:
            array.append(character)
    if translate:
        if html_mode:
            array.append("<br>")
        else:
            array.append("\n")
        array.append(string)
    return "".join(array)

def main(argv=[]):
    vinfo = tuple(str(x) for x in sys.version_info[:3])
    print("Reverse Alphabet Cipher (Python %s)" % (".".join(vinfo),))
    print("Enter blank input for options...")
    x = " ".join(argv)
    options = {"translation": False, "HTML mode": False}
    if len(x) == 0:
        x = input("> ")
    while 1:
        if x == "":
            y = input("Options\n%s\n>>> " % ("\n".join([x[0][0] + ": " + ("Disable " if x[1] else "Enable ") + x[0] for x in options.items()])))
            changed = False
            for key in options.keys():
                if y.lower() == str(key)[0].lower():
                    options[key] = not options[key]
                    print("%s %s." % (key.capitalize(), "enabled" if options[key] else "disabled"))
                    changed = True
                    break
            if not changed:
                print("Nothing changed.")
        else:
            print(decode(x, options["translation"], options["HTML mode"]))
        x = input("> ")

if __name__ == "__main__":
    main(sys.argv[1::])
