#!/usr/bin/env python3

import sys

rtable = "[bcdfghjklmnpqrstvwxyz][aeiou]"

table1={"ba": "B",
        "be": "[b]b[/b]",
        "bi": "[f]b[/f]",
        "bu": "[v]b[/v]",
        "by": "[f]b[/f]",
        "ca": "C",
        "ce": "[b]c[/b]",
        "ci": "[f]c[/f]",
        "cu": "[v]c[/v]",
        "cy": "[f]c[/f]",
        "da": "D",
        "de": "[b]d[/b]",
        "di": "[f]d[/f]",
        "du": "[v]d[/v]",
        "dy": "[f]d[/f]",
        "fa": "F",
        "fe": "[b]f[/b]",
        "fi": "[f]f[/f]",
        "fu": "[v]f[/v]",
        "fy": "[f]f[/f]",
        "ga": "G",
        "ge": "[b]g[/b]",
        "gi": "[f]g[/f]",
        "gu": "[v]g[/v]",
        "gy": "[f]g[/f]",
        "ha": "H",
        "he": "[b]h[/b]",
        "hi": "[f]h[/f]",
        "hu": "[v]h[/v]",
        "hy": "[f]h[/f]",
        "ja": "J",
        "je": "[b]j[/b]",
        "ji": "[f]j[/f]",
        "ju": "[v]j[/v]",
        "jy": "[f]j[/f]",
        "ka": "K",
        "ke": "[b]k[/b]",
        "ki": "[f]k[/f]",
        "ku": "[v]k[/v]",
        "ky": "[f]k[/f]",
        "la": "L",
        "le": "[b]l[/b]",
        "li": "[f]l[/f]",
        "lu": "[v]l[/v]",
        "ly": "[f]l[/f]",
        "ma": "M",
        "me": "[b]m[/b]",
        "mi": "[f]m[/f]",
        "mu": "[v]m[/v]",
        "my": "[f]m[/f]",
        "na": "N",
        "ne": "[b]n[/b]",
        "ni": "[f]n[/f]",
        "nu": "[v]n[/v]",
        "ny": "[f]n[/f]",
        "pa": "P",
        "pe": "[b]p[/b]",
        "pi": "[f]p[/f]",
        "pu": "[v]p[/v]",
        "py": "[f]p[/f]",
        "qa": "Q",
        "qe": "[b]q[/b]",
        "qi": "[f]q[/f]",
        "qu": "[v]q[/v]",
        "qy": "[f]q[/f]",
        "ra": "R",
        "re": "[b]r[/b]",
        "ri": "[f]r[/f]",
        "ru": "[v]r[/v]",
        "ry": "[f]r[/f]",
        "sa": "S",
        "se": "[b]s[/b]",
        "si": "[f]s[/f]",
        "su": "[v]s[/v]",
        "sy": "[f]s[/f]",
        "ta": "T",
        "te": "[b]t[/b]",
        "ti": "[f]t[/f]",
        "tu": "[v]t[/v]",
        "ty": "[f]t[/f]",
        "va": "V",
        "ve": "[b]v[/b]",
        "vi": "[f]v[/f]",
        "vu": "[v]v[/v]",
        "vy": "[f]v[/f]",
        "wa": "W",
        "we": "[b]w[/b]",
        "wi": "[f]w[/f]",
        "wu": "[v]w[/v]",
        "wy": "[f]w[/f]",
        "xa": "X",
        "xe": "[b]x[/b]",
        "xi": "[f]x[/f]",
        "xu": "[v]x[/v]",
        "xy": "[f]x[/f]",
        "ya": "Y",
        "ye": "[b]y[/b]",
        "yi": "[f]y[/f]",
        "yu": "[v]y[/v]",
        "yy": "[f]y[/f]",
        "za": "Z",
        "ze": "[b]z[/b]",
        "zi": "[f]z[/f]",
        "zu": "[v]z[/v]",
        "zy": "[f]z[/f]"}

table2={"bo": "[s]b[/s]",
        "co": "[s]c[/s]",
        "do": "[s]d[/s]",
        "fo": "[s]f[/s]",
        "go": "[s]g[/s]",
        "ho": "[s]h[/s]",
        "jo": "[s]j[/s]",
        "ko": "[s]k[/s]",
        "lo": "[s]l[/s]",
        "mo": "[s]m[/s]",
        "no": "[s]n[/s]",
        "po": "[s]p[/s]",
        "qo": "[s]q[/s]",
        "ro": "[s]r[/s]",
        "so": "[s]s[/s]",
        "to": "[s]t[/s]",
        "vo": "[s]v[/s]",
        "wo": "[s]w[/s]",
        "xo": "[s]x[/s]",
        "yo": "[s]y[/s]",
        "zo": "[s]z[/s]"}

table3={"ab": "°B",
        "eb": "[b]°b[/b]",
        "ib": "[f]°b[/f]",
        "ub": "[v]°b[/v]",
        "yb": "[f]°b[/f]",
        "ac": "°C",
        "ec": "[b]°c[/b]",
        "ic": "[f]°c[/f]",
        "uc": "[v]°c[/v]",
        "yc": "[f]°c[/f]",
        "ad": "°D",
        "ed": "[b]°d[/b]",
        "id": "[f]°d[/f]",
        "ud": "[v]°d[/v]",
        "yd": "[f]°d[/f]",
        "af": "°F",
        "ef": "[b]°f[/b]",
        "if": "[f]°f[/f]",
        "uf": "[v]°f[/v]",
        "yf": "[f]°f[/f]",
        "ag": "°G",
        "eg": "[b]°g[/b]",
        "ig": "[f]°g[/f]",
        "ug": "[v]°g[/v]",
        "yg": "[f]°g[/f]",
        "ah": "°H",
        "eh": "[b]°h[/b]",
        "ih": "[f]°h[/f]",
        "uh": "[v]°h[/v]",
        "yh": "[f]°h[/f]",
        "aj": "°J",
        "ej": "[b]°j[/b]",
        "ij": "[f]°j[/f]",
        "uj": "[v]°j[/v]",
        "yj": "[f]°j[/f]",
        "ak": "°K",
        "ek": "[b]°k[/b]",
        "ik": "[f]°k[/f]",
        "uk": "[v]°k[/v]",
        "yk": "[f]°k[/f]",
        "al": "°L",
        "el": "[b]°l[/b]",
        "il": "[f]°l[/f]",
        "ul": "[v]°l[/v]",
        "yl": "[f]°l[/f]",
        "am": "°M",
        "em": "[b]°m[/b]",
        "im": "[f]°m[/f]",
        "um": "[v]°m[/v]",
        "ym": "[f]°m[/f]",
        "an": "°N",
        "en": "[b]°n[/b]",
        "in": "[f]°n[/f]",
        "un": "[v]°n[/v]",
        "yn": "[f]°n[/f]",
        "ap": "°P",
        "ep": "[b]°p[/b]",
        "ip": "[f]°p[/f]",
        "up": "[v]°p[/v]",
        "yp": "[f]°p[/f]",
        "aq": "°Q",
        "eq": "[b]°q[/b]",
        "iq": "[f]°q[/f]",
        "uq": "[v]°q[/v]",
        "yq": "[f]°q[/f]",
        "ar": "°R",
        "er": "[b]°r[/b]",
        "ir": "[f]°r[/f]",
        "ur": "[v]°r[/v]",
        "yr": "[f]°r[/f]",
        "as": "°S",
        "es": "[b]°s[/b]",
        "is": "[f]°s[/f]",
        "us": "[v]°s[/v]",
        "ys": "[f]°s[/f]",
        "at": "°T",
        "et": "[b]°t[/b]",
        "it": "[f]°t[/f]",
        "ut": "[v]°t[/v]",
        "yt": "[f]°t[/f]",
        "av": "°V",
        "ev": "[b]°v[/b]",
        "iv": "[f]°v[/f]",
        "uv": "[v]°v[/v]",
        "yv": "[f]°v[/f]",
        "aw": "°W",
        "ew": "[b]°w[/b]",
        "iw": "[f]°w[/f]",
        "uw": "[v]°w[/v]",
        "yw": "[f]°w[/f]",
        "ax": "°X",
        "ex": "[b]°x[/b]",
        "ix": "[f]°x[/f]",
        "ux": "[v]°x[/v]",
        "yx": "[f]°x[/f]",
        "ay": "°Y",
        "ey": "[b]°y[/b]",
        "iy": "[f]°y[/f]",
        "uy": "[v]°y[/v]",
        "yy": "[f]°y[/f]",
        "az": "°Z",
        "ez": "[b]°z[/b]",
        "iz": "[f]°z[/f]",
        "uz": "[v]°z[/v]",
        "yz": "[f]°z[/f]"}

table4={"ob": "[s]°b[/s]",
        "oc": "[s]°c[/s]",
        "od": "[s]°d[/s]",
        "of": "[s]°f[/s]",
        "og": "[s]°g[/s]",
        "oh": "[s]°h[/s]",
        "oj": "[s]°j[/s]",
        "ok": "[s]°k[/s]",
        "ol": "[s]°l[/s]",
        "om": "[s]°m[/s]",
        "on": "[s]°n[/s]",
        "op": "[s]°p[/s]",
        "oq": "[s]°q[/s]",
        "or": "[s]°r[/s]",
        "os": "[s]°s[/s]",
        "ot": "[s]°t[/s]",
        "ov": "[s]°v[/s]",
        "ow": "[s]°w[/s]",
        "ox": "[s]°x[/s]",
        "oy": "[s]°y[/s]",
        "oz": "[s]°z[/s]"}

table5={"a": "α",
        "e": "ε",
        "i": "ι",
        "o": "ο",
        "u": "υ"}

table6={"[s]": "[strike]",
        "[/s]": "[/strike]",
        "[f]": "[i]",
        "[/f]": "[/i]",
        "[v]": "[u]",
        "[/v]": "[/u]"}

def decode(string):
    string = string.lower()
    brf = []
    nstring = string.split()
    for lstring in nstring:
        for dic in (table1,table2,table3,table4,table5,table6):
            for key in dic.keys():
                if key in lstring:
                    lstring = lstring.replace(key, dic[key])
        brf.append(lstring)
    return " ".join(brf)

def main(argv=[]):
    x = " ".join(argv)
    if len(x) == 0:
        x = input("> ")
    while 1:
        print(decode(x))
        x = input("> ")

if __name__ == "__main__":
    main(sys.argv[1::])
