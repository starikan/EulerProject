# -*- coding: utf-8 -*-
__author__ = 'Starik'

import math

def mainFunc():
    nums = []
    for i in xrange(3, 100000):
        s = sum([math.factorial(int(j)) for j in str(i)])
        if s == i:
            nums.append(s)
    print sum(nums)

if __name__ == "__main__":
    mainFunc()