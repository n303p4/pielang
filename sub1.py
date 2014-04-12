#!/usr/bin/env python3

# Pielang
# Public domain

import sys, traceback
import re

def chop(thestring, ending):
  if thestring.startswith(ending):
    return thestring[len(ending):]
  return thestring

def rchop(thestring, ending):
  if thestring.endswith(ending):
    return thestring[:-len(ending)]
  return thestring

doubleReplace = {"o": "a",
                 "a": "e",
                 "e": "i",
                 "u": "u",
                 "f": "g",
                 "g": "q",
                 "q": "f"}

doubleReplace2 = {"vei": "bei",
                 "twe": "vei",
                 "two": "due",
                 "on": "ein",
                 "th": "d",
                 "ll": "rl",
                 "ld": "lt",
                 "nt": "nd",
                 "gi": "jei",
                 "wor": "wer",
                 "fo": "vie",
                 "fir": "for",
                 "ni": "nei",
                 "an": "un",
                 "ave": "afe",
                 "ive": "ife",
                 "lve": "lfe",
                 "x": "ks",
                 "ght": "cht",
                 "ee": "ie",
                 "ty": "tiene"}

doubleReplace3 = {}

badStarts = {"w": "sw"}

badEndings = {}

def decode(string):
    nstring = string.split()
    brf = []
    for string in nstring:
        lstring = string
        for dic in (doubleReplace, doubleReplace2, doubleReplace3):
            for char in range(0,len(lstring)):
                for key in dic.keys():
                    try: x = lstring[char:char+len(key)]
                    except: pass
                    else:
                        if x == key:
                            lstring = lstring.replace(key, dic[key], 1)
                            char += len(dic[key])
                        elif x.lower() == key:
                            lstring = lstring.replace(key, dic[key].capitalize(), 1)
                            char += len(dic[key])
        for key in badEndings.keys():
            if lstring.endswith(key) and len(lstring) > len(key):
                lstring = lstring[:-len(key)] + badEndings[key]
            for k in ("title", "upper"):
                if lstring.endswith(eval("\"%s\".%s()" % (key, k))) and len(lstring) > len(key):
                    lstring = lstring[:-len(key)] + eval("\"%s\".%s()" % (badEndings[key], k))
        for key in badStarts.keys():
            if lstring.startswith(key) and len(lstring) > len(key):
                lstring = badStarts[key] + lstring[len(key):]
            for k in ("title", "upper"):
                if lstring.startswith(eval("\"%s\".%s()" % (key, k))) and len(lstring) > len(key):
                    lstring = eval("\"%s\".%s()" % (badStarts[key], k)) + lstring[len(key):]
        if lstring in ("i", "I"):
            lstring = "nie"
        brf.append(lstring)
    return " ".join(brf)

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("Enter string here: ")
    print(decode(x))

if __name__ == "__main__":
    main(sys.argv[1::])
