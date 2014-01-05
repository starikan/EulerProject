# -*- coding: utf-8 -*-
__author__ = 'Starik'

# import framework as fr
# import itertools as it

# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     return chain.from_iterable(combinations(s, r) for r in range(2,len(s)+1))

# def triangNum(maxNum):
#     i = 1L
#     triang = i
#     while i<maxNum:
#         yield triang
#         i += 1
#         triang += i


#for num in triangNum(100000):
##    print num
#    if num>=223092870: #2*3*5*7*11*13*17*19*23
#
#        prime = fr.MathClass().primeListUpTo(1+num/2)
#        fact = [pr for pr in prime if int(num*1./pr)-num*1./pr == 0.0]
#
#        for i in powerset(fact):
#            prod = reduce(lambda x,y:x*y, i)
#    #        print i, prod
#            if prod<num:
#                fact.append(prod)
#
#        fact += [1, num]
#        print len(fact), num, fact

# def genTriang(num):
#     for n in xrange(num):
#         yield (n+1)*n/2


# def powerset(iterable):
#     "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
#     s = list(iterable)
#     pList = list(set([i for i in it.chain.from_iterable(it.combinations(s, r) for r in range(len(s)+1))]))
#     pList = [reduce(lambda x,y: x*y, i) for i in pList if i]
#     return pList


# def div(N, I, primes):
#     for p in primes:
#         if not N % p:
#             I += 1
#             print "N = {}, p = {}, N/p = {}, I = {}".format(N, p, N/p, I)
#             div(N / p, I, primes)
#         else:
#             pass
#     return I


# triang = ((n+1)*n/2 for n in xrange(1, 10))

# pClass = fr.MathClass()
# for i in triang:
#     print "Triang = ", i
#     primes = pClass.primeListUpTo(i)
#     primesPow = []
#     for p in primes:
#         pow = 1
#         while i > 1:
#             pow += 1
#             i = i / p
#             if i % p:
#                 break
#             else:
#                 pass
#         primesPow.append(pow)
#     print primes
#     print primesPow
# Математически :это надо разложить на произведение степеней простых чисел (а по основной теореме арифметики любое натуральное число можно так представить), и количество делителей этого числа равно произведению чисел,каждое из которых есть встречающаяся степень плюс один.
# то есть например у числа 2^5 * 3^4 * 7^2 будет количество делителей: 6*5*3
# Вообщем : длинная арифметика в факторизованном виде.
def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1
        if d * d > n:
            if n > 1:
                factors.append(n)
            break
    return factors

n, summ = 0, 0

while n < 5000 and summ < 501:
    n += 1
    factor = prime_factors((n + 1) * n / 2)
    counts = [factor.count(j) for j in set(factor)]
    summ = sum(j + 1 for j in counts)
    if not n % 100:
        print "Number:", n, "Factor:", factor, "Counts:", counts, "Sum:", summ
print n
