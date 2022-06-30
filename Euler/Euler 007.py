# -*- coding: utf-8 -*-
__author__ = 'Starik'

import sys
sys.path.append('../')
import framework as fr

if __name__ == "__main__":
    mathR = fr.MathClass()
    print len(mathR.primeListCount(100000))