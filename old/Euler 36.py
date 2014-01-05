# -*- coding: utf-8 -*-
__author__ = 'Starik'

def mainFunc():
    seq = []
    for i in xrange(1, 1000001):
        i10 = str(i)
        i2 = bin(i)[2:]
        if i10 == i10[::-1] and i2 == i2[::-1]:
            seq.append(i)
    print sum(seq)
if __name__ == "__main__":
    mainFunc()