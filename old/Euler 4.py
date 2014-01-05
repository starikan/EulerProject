# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 02:07:34 2012

@author: Starik
"""

def factor(num):
    for i in xrange(999, 100, -1):
        if not num%i and 999>num/i>99:
            print "Factorization: {0}, {1}".format(i, num/i)
            return 1
    return 0
def yRange(start, end):
    for i in xrange(start, end, -1):
        if str(i)[::-1] == str(i):
            yield i
r = yRange(999999, 100000)
for i in r:
    if factor(i):
        print "Palindrome:    {0}".format(i)
        break