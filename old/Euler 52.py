# -*- coding: utf-8 -*-
__author__ = 'Starik'

def mainFunc():
    i = 1
    while not set(str(i)) == set(str(2*i)) == set(str(3*i)) == set(str(4*i)) == set(str(5*i)) == set(str(6*i)):
        i += 1
    print i

if __name__ == "__main__":
    mainFunc()