# -*- coding: utf-8 -*-
__author__ = 'Starik'


# Ишмухаметов Ш.Т. глава 1.2
def powerMod(a, b, m): # a**b mod m
    b = [bool(int(i)) for i in bin(b)[3:]] # 0b1111101011 -> 0b1[111101011] -> [True, False, ...]
    a0 = a
    for i in b:
        if i:
            a = (a**2 * a0) % m
        else:
            a = a**2 % m
    return a


if __name__ == "__main__":
    print powerMod(2, 199, 1003)
    print powerMod(2, 7830457, 10**10)*28433 + 1
    print pow(2, 7830457) % 10**10 *28433 + 1