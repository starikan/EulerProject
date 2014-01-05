# -*- coding: utf-8 -*-
__author__ = 'Starik'

import datetime
import framework as fr

primes = fr.MathClass().primeListUpTo(1000)
primes.reverse()
res = []
number, length = 0, 0
startTime = prev = datetime.datetime.now()

for i, item in enumerate(primes):
    now = datetime.datetime.now()
    delta = prev - now
    if delta.seconds > 20:
        prev = datetime.datetime.now()
        allTime = now - startTime
        print item, allTime.seconds/60, length, number

    for start in xrange(i+1, len(primes)-1):
        add = max(item/primes[start], length)
        for end in xrange(start + add, len(primes)-1):
            summ = sum(primes[start: end])
            if summ > item:
                break
            elif summ == item:
                res.append([item, len(primes[start: end]), primes[start: end]])
                if len(primes[start: end]) > length:
                    length = len(primes[start: end])
                    number = item
# for i in res:
    # print (i)

print length, number
