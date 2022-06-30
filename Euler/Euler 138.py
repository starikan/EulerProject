# -*- coding: utf-8 -*-
__author__ = 'Starik'

def fib(n):
     if n==1 or n==2:
         return 1
     return fib(n-1) + fib(n-2)

def fib2(n):
    a,b = 1,1
    while a < n:
        yield a
        a,b = b,a+b

#print [(y**2-x**2, 2*x*y, x**2+y**2) for x in xrange(1,1000) for y in xrange(x+1,1000) if 4*x*y==y**2-x**2-1 or 4*x*y==y**2-x**2+1]
#print [(y**2-x**2, 2*x*y, x**2+y**2) for x in xrange(1,1000) for y in xrange(x+1,1000) if 4*x*y==y**2-x**2-1]
#print [(y**2-x**2, 2*x*y, x**2+y**2) for x in xrange(1,1000) for y in xrange(x+1,1000) if 4*x*y==y**2-x**2+1]

