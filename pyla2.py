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

replacement_table = {"a": "ao",
                     "b": "c",
                     "c": "va",
                     "d": "t",
                     "e": "i",
                     "f": "g",
                     "g": "h",
                     "h": "y",
                     "i": "e",
                     "j": "k",
                     "k": "li",
                     "l": "p",
                     "m": "n",
                     "n": "m",
                     "o": "a",
                     "p": "q",
                     "q": "z",
                     "r": "sh",
                     "s": "ez",
                     "t": "d",
                     "u": "u",
                     "v": "w",
                     "w": "r",
                     "x": "j",
                     "y": "ie",
                     "z": "f"}

doubleReplace = {"hm": "hem",
                 "aao": "a",
                 "vaeao": "vao",
                 "ieau": "yao",
                 "hh": "h'h",
                 "tsh": "tash",
                 "csh": "cash",
                 "hup": "hurp",
                 "aomt": "ont",
                 "ryao": "rao",
                 "aoie": "ie",
                 "iao": "a",
                 "au": "ao",
                 "emg": "eng",
                 "dsh": "dish",
                 "yi": "ie",
                 "ii": "ie",
                 "uao": "ao",
                 "vaa": "va",
                 "ziwi": "zwi",
                 "zdsh": "zdesh",
                 "zye": "zie",
                 "shsh": "sh",
                 "pez": "pz"}

doubleReplace2 = {"iee": "ie'e",
                  "pao": "po",
                  "ea": "ia",
                  "hih": "h",
                  "deshu": "desh",
                  "ye": "ie'e"}

doubleReplace3 = {"eez": "ez",
                  "hyd": "haed"}

badStarts = {"ez": "z",
             "gew": "gw",
             "iau": "yao",
             "dya": "dia",
             "dys": "dis",
             "iei": "ie",
             "iee": "ie'e",
             "ieao": "iao",
             "qs": "meqs",
             "qy": "eqy"}

badEndings = {"aop": "ao",
              "pt": "t",
              "shit": "shift",
              "dy": "die",
              "yam": "iam",
              "ay": "ae",
              "aedez": "aedz",
              "eam": "iam",
              "emh": "em",
              "hy": "hie",
              "i": "ir"}

def decode(string):
    nstring = string.split()
    brf = []
    for string in nstring:
        lstring = list(string)
        for index in range(0, len(lstring)):
            char = lstring[index]
            try: char2 = lstring[index-1]
            except: char2 = ""
            else:
                if char2 != "e":
                    char2 = ""
            if char in replacement_table.keys():
                lstring[index] = replacement_table[char].replace(char2, "")
            elif char.lower() in replacement_table.keys():
                lstring[index] = replacement_table[char.lower()].replace(char2, "").title()
        lstring = "".join(lstring)
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
        lstring = lstring.replace("ie'e", "'ye")
        if lstring == "E":
            lstring = "Nie"
        elif lstring == "aom":
            lstring = "nek"
        elif lstring == "Aom":
            lstring = "Nek"
        elif lstring == "aon":
            lstring = "nem"
        elif lstring == "Aon":
            lstring = "Nem"
        brf.append(lstring)
    return " ".join(brf).replace(" .", ".").replace(" !", "!").replace(" ,", ",").replace(" ?", "?")

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("Enter string here: ")
    print(decode(x))

if __name__ == "__main__":
    main(sys.argv[1::])
