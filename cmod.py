#!/usr/bin/env python3

import sys

table1={"good": "☺",
 "happy": "☺",
 "bad": "☹",
 "sad": "☹",
 "girl": "♀",
 "female": "♀",
 "woman": "♀",
 "boy": "♂",
 "male": "♂",
 "man": "♂",
 "lesbian": "⚢",
 "gay": "⚣",
 "bisexual": "⚤",
 "transgender": "⚥",
 "agender": "⚪",
 "asexual": "⚪",
 "neuter": "⚪",
 "caution": "⚠",
 "warning": "⚠",
 "look out": "⚠"}

table2={"th": "þ",
 "ba": "バ",
 "bu": "ブ",
 "ce": "ɔ",
 "co": "ᴒ",
 "du": "ヅ",
 "do": "ド",
 "fe": "ɟ",
 "fu": "フ",
 "ge": "ᵷ",
 "ha": "ハ",
 "he": "ɥ",
 "hu": "フ",
 "ke": "ʞ",
 "la": "‒",
 "lo": "‒",
 "le": "ꞁ",
 "me": "ɯ",
 "mo": "ᴟ",
 "na": "ナ",
 "ne": "ネ",
 "no": "ノ",
 "nu": "ヌ",
 "pa": "パ",
 "pu": "プ",
 "re": "ɹ",
 "ta": "タ",
 "te": "ʇ",
 "to": "ト",
 "ve": "ʌ",
 "we": "ʍ",
 "wo": "Σ",
 "ye": "ʎ",
 "za": "ɴ",
 "zo": "ɴ",
 "?!": "‽",
 "!?": "‽"}
 
table3={"bi": "b",
 "by": "b",
 "be": "q",
 "ci": "c",
 "cy": "c",
 "de": "p",
 "di": "d",
 "dy": "d",
 "fi": "f",
 "fy": "f",
 "gi": "g",
 "gy": "g",
 "hi": "h",
 "hy": "h",
 "ji": "j",
 "jy": "j",
 "ki": "k",
 "ky": "k",
 "li": "l",
 "ly": "l",
 "mi": "m",
 "my": "m",
 "ni": "n",
 "ny": "n",
 "pi": "p",
 "py": "p",
 "pe": "d",
 "qi": "q",
 "qy": "q",
 "qe": "b",
 "ri": "r",
 "ry": "r",
 "si": "s",
 "sy": "s",
 "se": "s",
 "ti": "t",
 "ty": "t",
 "vi": "v",
 "vy": "v",
 "wi": "w",
 "wy": "w",
 "xi": "x",
 "xy": "x",
 "yi": "y",
 "yy": "y",
 "zi": "z",
 "zy": "z",
 "ze": "z"}

def decode(string):
    string = string.lower()
    brf = []
    nstring = string.split()
    for lstring in nstring:
        for dic in (table1, table2, table3):
            for key in dic.keys():
                if key in lstring:
                    lstring = lstring.replace(key, dic[key], 1)
        brf.append(lstring)
    return " ".join(brf)

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("Enter string here: ")
    print(decode(x))

if __name__ == "__main__":
    main(sys.argv[1::])
