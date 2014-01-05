# -*- coding: utf-8 -*-
__author__ = 'Starik'

def mainFunc():
    nums = [(sum([int(j)**5 for j in str(i)]), i) for i in xrange(2, 1000000)]
    seq = [j for i,j in nums if i == j]
    print seq, sum(seq)

if __name__ == "__main__":
    mainFunc()