# -*- coding: utf-8 -*-
__author__ = 'Starik'

def mainFunc():
    s = "."
    i = 1
    while len(s) < 1000001:
        s += str(i)
        i += 1
    print int(s[1]) * int(s[10]) * int(s[100]) * int(s[1000]) * int(s[10000]) * int(s[100000]) * int(s[1000000])

if __name__ == "__main__":
    mainFunc()