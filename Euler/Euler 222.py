# -*- coding: utf-8 -*-
__author__ = 'Starik'

import math

def mainFunc():
    D = 100.0
    r = [i for i in xrange(30,51)]
    l = [math.sqrt(1 - ( (D - r[i] - r[i+1]) / (r[i] + r[i+1]) ) ** 2) * (r[i] + r[i+1]) for i in xrange(len(r)-1)]

    print sum(r)
    print l
    print (sum(l) + r[0] + r[-1])*1000


if __name__ == "__main__":
    mainFunc()