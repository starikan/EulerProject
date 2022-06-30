import math

from primes import primes


primes = primes()
primes.extend()
print(primes)

n = 1
for i in range(2, 1000):
    n += i
    primes.extend(grow_upto=n)
    



# dividers = {1: 1}
# n = 1

# for i in range(2, 100000):
#     n += i

#     dividers_new = 0
#     start = 0
#     # for f in list(dividers.keys())[::-1]:
#     #     if n % f == 0:
#     #         dividers_new = dividers[f]
#     #         start = f
#     #         break

#     # print(n, start, dividers_new)

#     divs = []
#     for d in range(1, int(math.sqrt(n) + 1) + 1):
#         if n % d == 0:
#             divs.append(d)
#             dividers_new += 1
#     divs.append(n)
#     if (len(divs) > 100):
#         print(len(divs), n)
#     if (len(divs) > 500):
#         break
#     dividers[n] = dividers_new + 1 