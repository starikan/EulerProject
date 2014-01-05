# -*- coding: utf-8 -*-
__author__ = 'Starik'

import numpy as np

def fib_num(n):
    arr = np.zeros(n)
    arr[0] = 1
    arr[1] = 1
    for index in range(2,n):
        arr[index] = arr[index-1] + arr[index-2]
    return arr[n-1] # Return nth Fibonacci number. 

def fib2(n):
    a,b = 1,1
    while a < n:
        yield a
        a,b = b,a+b

# def fib(n):
#     a, b = 0, 1
#     for _ in xrange(n):
#         yield a
#         a, b = b, a + b

# print list(fib(10000))[-1]

# print [i for i in fib2(math.pow(10, 1000))]
# print fib_num(1000)

a, b, i = 0, 1, 0
while len(str(a))<1000:
    a, b, i = b, a + b, i + 1
print i, a

