#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# "Standard Abugida"

import sys, re

rtable = "[bcdfghjklmnpqrstvwxyz][a]"

table0={"y": "i"}

table1 = {"ba": "β",
          "ca": "χ",
          "da": "δ",
          "fa": "φ",
          "ga": "γ",
          "ha": "η",
          "ja": "ϳ",
          "ka": "κ",
          "la": "λ",
          "ma": "μ",
          "na": "ν",
          "pa": "π",
          "qa": "ϟ",
          "ra": "ρ",
          "sa": "σ",
          "ta": "τ",
          "va": "ϐ",
          "wa": "ω",
          "xa": "ξ",
          "za": "ζ",
          "[bcdfghjklmnpqrstvwxz]e": "[b]%s[/b]",
          "[bcdfghjklmnpqrstvwxz]i": "[f]%s[/f]",
          "[bcdfghjklmnpqrstvwxz]o": "[s]%s[/s]",
          "[bcdfghjklmnpqrstvwxz]u": "[v]%s[/v]"}

table2 = {"ab": "°β",
          "ac": "°χ",
          "ad": "°δ",
          "af": "°φ",
          "ga": "°γ",
          "ha": "°η",
          "ja": "°ϳ",
          "ka": "°κ",
          "la": "°λ",
          "ma": "°μ",
          "na": "°ν",
          "pa": "°π",
          "qa": "°ϟ",
          "ra": "°ρ",
          "sa": "°σ",
          "ta": "°τ",
          "va": "°ϐ",
          "wa": "°ω",
          "xa": "°ξ",
          "za": "°ζ",
          "e[bcdfghjklmnpqrstvwxz]": "[b]°%s[/b]",
          "i[bcdfghjklmnpqrstvwxz]": "[f]°%s[/f]",
          "o[bcdfghjklmnpqrstvwxz]": "[s]°%s[/s]",
          "u[bcdfghjklmnpqrstvwxz]": "[v]°%s[/v]"}

table5={"a": "α",
        "e": "ε",
        "i": "ι",
        "o": "ο",
        "u": "υ"}

table6={"\[s\]": "[strike]",
        "\[/s\]": "[/strike]",
        "\[f\]": "[i]",
        "\[/f\]": "[/i]",
        "\[v\]": "[u]",
        "\[/v\]": "[/u]"}

table7=["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]

def decode(string, translate=False, html_mode=False):
    brf = []
    nstring = string.split()
    for lstring in nstring:
        for dic in (table0,table1,table2,table5,table6,table7):
            if type(dic) is list:
                for char in dic:
                    lstring = lstring.replace(char, "↑" + char.lower())
            else:
                for key in dic.keys():
                    r = dic[key]
                    if html_mode:
                        r = r.replace("[", "<").replace("]", ">")
                    for match in re.findall(key, lstring):
                        lstring = lstring.replace(match, (r % (match[0],) if "%s" in r else r))
                    if key.capitalize() in lstring:
                        if "[/" in r:
                            lstring = lstring.replace(key.capitalize(), r.replace("]", "]↑", 1))
                        else:
                            lstring = lstring.replace(key.capitalize(), "↑" + r)
        if html_mode:
            lstring = list(lstring)
            for i in range(0, len(lstring)):
                if not re.match("[1-9a-zA-Z\]\[/!?\"'.,()<>]", lstring[i]):
                    try: lstring[i] = "&#%s;" % (ord(lstring[i]),)
                    except: print(lstring[i])
            lstring = "".join(lstring)
        brf.append(lstring)
    return " ".join(brf) + ("\n[i]%s[/i]" % (string,) if translate else "")

def main(argv=[]):
    vinfo = tuple(str(x) for x in sys.version_info[:3])
    print("Standard Abugida Converter (Python %s)" % (".".join(vinfo),))
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
