# -*- coding: utf-8 -*-
__author__ = 'Starik'

import sys
sys.path.append("..")
import framework as f

def mainFunc():
    primes = f.MathClass().primeListUpTo(1000000)
    pCirc = []
    pSet = set(primes)
    for p in primes:
        p = str(p)
        pRotate = all([int(p[i:]+p[:i]) in pSet for i in range(len(p))])
        if pRotate:
            pCirc.append(pRotate)
    print len(pCirc)
if __name__ == "__main__":
    mainFunc()