# -*- coding: utf-8 -*-
__author__ = 'Starik'

import time
now = time.time()


#cache = []
#
#def collatz(n):
#    i = 0
#    while n>1 or n>len(cache):
#        i += 1
#        n = n%2 * (3*n + 1) - (n%2 - 1) * n/2
#    if n<=1:
#        return i
#    else:
#        return i + cache[n]
#
#def main():
#    for i in xrange(100000):
#        cache.append(collatz(i))
#    print max(cache)


#if __name__ == "__main__":
#    from timeit import Timer
#    t = Timer("main()", "from __main__ import main")
#    print t.timeit(1)


def next(n):
    if n % 2:
        return 3 * n + 1
    else:
        return n / 2

class ChainCache:
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n == 1:
            return 1
        elif n in self.cache:
            return self.cache[n]
        else:
            c = self.__call__(next(n))
            self.cache[n] = c + 1
            return c + 1

chainlen = ChainCache()

def maxlen(x):
    m = 0
    v = 0
    for i in range(1, x):
        l = chainlen(i)
        if l > m:
            m = l
            v = i
    return v, m

print maxlen(1000000)

print "Вермя прошло: ", time.time() - now