# -*- coding: utf-8 -*-
__author__ = 'Starik'

def mainFunc():
    print len(set([a**b for a in xrange(2, 101) for b in xrange(2, 101)]))

if __name__ == "__main__":
    mainFunc()