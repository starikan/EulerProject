# -*- coding: utf-8 -*-
__author__ = 'Starik'

dig = set("123456789")

def getPan(n): # n*1 & n*2 & n*3 & ... & n*l
    s = ""
    for i in xrange(1, 10):
        s += str(n*i)
        if len(s) > 9:
            break
        elif len(s) == 9 and set(s) == dig:
            return int(s)

def mainFunc():
    pandigital = []
    for k in xrange(1, 10000):
        p = getPan(k)
        if p:
            pandigital.append(p)
    print max(pandigital)

if __name__ == "__main__":
    mainFunc()