# -*- coding: utf-8 -*-
"""
Created on Sun Feb 05 01:29:31 2012

@author: Starik
"""

# Euler 3
# http://rebrained.com/?p=458
import numpy
import math

def prime6(upto):
    primes=numpy.arange(3,upto+1,2)
    isprime=numpy.ones((upto-1)/2,dtype=bool)
    for factor in primes[:int(math.sqrt(upto))]:
        if isprime[(factor-2)/2]: isprime[(factor*3-2)/2::factor]=0
    return numpy.insert(primes[isprime],0,2)

N = 600851475143
prime = 1
primes = prime6(50000)
for i in primes:
    if not N%i:
        N = N/i
        prime = i
print primes
print N, prime

