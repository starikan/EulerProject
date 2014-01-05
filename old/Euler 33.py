# -*- coding: utf-8 -*-
__author__ = 'Starik'

import itertools as it

def mainFunc():
    p = 1.
    for x in it.product(xrange(10, 100), repeat=2):
        i, j = x
        iS, jS = str(i), str(j)
        cross = set(iS).intersection(set(jS))
        if i != j and len(cross) >= 1 and i%10 and j%10:
#            print x, cross
            for c in cross:
                if i*1./j == float(iS.replace(c,"",1))/float(jS.replace(c,"",1)) < 1:
                    print i, j, c, i*1./j
                    p *= (i*1./j)
    print p


if __name__ == "__main__":
    mainFunc()