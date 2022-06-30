# -*- coding: utf-8 -*-
__author__ = 'Starik'

lychrel = []

def mainFunc():
    for i in xrange(10000):
        next = i
        for j in xrange(51):
            next += int(str(next)[::-1])
            if str(next) == str(next)[::-1]:
                break
        if j>=50:
            lychrel.append(i)
    print len(lychrel)
    print lychrel

if __name__ == "__main__":
    mainFunc()