# -*- coding: utf-8 -*-
__author__ = 'Starik'

import sys
sys.path.append('../')
import framework as fr
import math

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a*b/gcd(a, b)

if __name__ == "__main__":
    fMath = fr.MathClass()
    print(reduce(lambda x,y: x*y, [i**int(math.log(20, i)) for i in fMath.primeList(20)])) # My solution

    print reduce(lcm, range(1, 20+1))
