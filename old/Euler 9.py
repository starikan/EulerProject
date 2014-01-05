# -*- coding: utf-8 -*-
"""
Created on Thu Feb 09 10:37:04 2012

@author: Starik
"""

#def abc(a, b, c):
#    while a+b+c<=1000:# and a**2+b**2>=c**2:
#        yield (a, b, c)
#        c += 1
#        if a+b+c>1000:
#            b += 1
#            c = b+1
#        
#
#for a in xrange(1,5000):    
#    for i in abc(a, a+1, a+2):
##        print i
#        if i[0]**2 + i[1]**2 == i[2]**2:
##            print i, sum(i)
#            if sum(i)==1000: 
#                print "===> ",i, i[0]*i[1]*i[2]
#                break
            
print [(x,y,1000-x-y) for x in xrange(1,1000) for y in xrange(1,x) if x**2+y**2==(1000-x-y)**2]