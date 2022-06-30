# -*- coding: utf-8 -*-
__author__ = 'Starik'

sq1 = sum([i ** 2 for i in range(1,101)])
sq2 = (sum([i for i in range(1,101)])) ** 2
print sq2 - sq1