#!/usr/bin/env python3

# Pielang
# Public domain

import sys, traceback

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
good_starts = ["dh", "th", "st", "dw", "wh", "kw", "br"]
bad_endings = {"eiw": "iew", "bd": "bed", "eiwn": "ein"}
bad_starts = {"ieei": "ieu"}

def chop(thestring, ending):
  if thestring.startswith(ending):
    return thestring[len(ending):]
  return thestring

def rchop(thestring, ending):
  if thestring.endswith(ending):
    return thestring[:-len(ending)]
  return thestring

replacement_table = {"a": "a",
                     "b": "b",
                     "c": "g",
                     "d": "t",
                     "e": "a",
                     "f": "v",
                     "g": "k",
                     "h": "h",
                     "i": "e",
                     "j": "j",
                     "k": "k",
                     "l": "r",
                     "m": "anta",
                     "n": "n",
                     "o": "ei",
                     "p": "b",
                     "q": "kw",
                     "r": "r",
                     "s": "s",
                     "t": "d",
                     "u": "u",
                     "v": "f",
                     "w": "w",
                     "x": "ks",
                     "y": "ie",
                     "z": "c"}

def decode(string):
    nstring = string.split()
    brf = []
    for string in nstring:
        if string == "my":
            string = "Ik's"
        elif string == "My":
            string = "Ik's"
        lstring = list(string.replace("ou", "o").replace("oo", "uu").replace("tt", "t").replace("ll", "l").replace("ff", "f"))
        for index in range(0, len(lstring)):
            char = lstring[index]
            if char in replacement_table.keys():
                lstring[index] = replacement_table[char]
            elif char.lower() in replacement_table.keys():
                lstring[index] = replacement_table[char.lower()].title()
        lstring = list("".join(lstring))
        if len(lstring) == 1:
            if lstring[0] in ("I", "E"):
                lstring[0] = "Ek"
            elif lstring[0] == "a":
                lstring[0] = "an"
        elif lstring[0] == "An":
            lstring[0] = "An"
        if lstring[0] in consonants:
            try: lstring[1]
            except: pass
            else:
                if lstring[1] in consonants and lstring[0] + lstring[1] not in good_starts:
                    lstring.insert(0, "e")
        elif lstring[0].lower() in consonants:
            try: lstring[1]
            except: pass
            else:
                if lstring[1] in consonants and (lstring[0] + lstring[1]).lower() not in good_starts:
                    lstring[0] = lstring[0].lower()
                    lstring.insert(0, "E")
        try: byoop = (lstring[-1].lower() == "." and lstring[-2].lower() == ":")
        except: byoop = False
        if lstring[-1].lower() == ":" or byoop:
            lstring.pop()
            if lstring[-1] == ":":
                lstring[-1] = "."
            if lstring[0] in vowels:
                lstring.insert(0, "en")
            elif lstring[0].lower() in vowels:
                lstring[0] = lstring[0].lower()
                lstring.insert(0, "En")
            elif lstring[0] in consonants:
                lstring.insert(0, "e")
            elif lstring[0].lower() in consonants:
                lstring[0] = lstring[0].lower()
                lstring.insert(0, "E")
            else:
                lstring.insert(0, "e")
        prefinal = "".join(lstring)
        for key in bad_starts:
            if prefinal.startswith(key):
                prefinal = bad_starts[key] + chop(prefinal, key)
                break
            elif prefinal.lower().startswith(key):
                prefinal = bad_starts[key].capitalize() + chop(prefinal, key.capitalize())
                break
        for key in bad_endings:
            if prefinal.endswith(key):
                prefinal = rchop(prefinal, key) + bad_endings[key]
                break
            elif prefinal.endswith(key):
                prefinal = rchop(prefinal, key) + bad_endings[key]
                break
        brf.append(prefinal)
    return " ".join(brf)

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("Enter string here: ")
    print(decode(x))

if __name__ == "__main__":
    main(sys.argv[1::])
