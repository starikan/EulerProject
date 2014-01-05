# -*- coding: utf-8 -*-
__author__ = 'Starik'

def mainFunc():
    pow = [a**b for a in xrange(90, 100) for b in xrange(90, 100)]
    summs = [sum([int(s) for s in str(p)]) for p in pow]
    print max(summs)

if __name__ == "__main__":
    mainFunc()