import sys

for line in sys.stdin:
  leters = line.rstrip()
  if not leters or len(leters) > 1000000:
    print("-1")
    sys.exit(0)
  else:
    T = len([i for i in leters if i == 'T'])
    M = len([i for i in leters if i == 'M'])
    C = len([i for i in leters if i == 'C'])

    if T + M + C != len(leters):
      print("-1")
      sys.exit(0)

    oddT = T % 2
    oddM = M % 2
    oddC = C % 2

    if oddT + oddM + oddC > 1:
      print("-1")
      sys.exit(0)
    else:
      result = ''
      if (oddT):
        result += 'T' * T
        result = ('M' * (M//2)) + result + ('M' * (M//2))
        result = ('C' * (C//2)) + result + ('C' * (C//2))
        print(result)
        sys.exit(0)
      if (oddM):
        result += 'M' * M
        result = ('T' * (T//2)) + result + ('T' * (T//2))
        result = ('C' * (C//2)) + result + ('C' * (C//2))
        print(result)
        sys.exit(0)
      if (oddC):
        result += 'C' * C
        result = ('T' * (T//2)) + result + ('T' * (T//2))
        result = ('M' * (M//2)) + result + ('M' * (M//2))
        print(result)
        sys.exit(0)
      if result == '':
        result += 'T' * T
        result = ('M' * (M//2)) + result + ('M' * (M//2))
        result = ('C' * (C//2)) + result + ('C' * (C//2))
        print(result)
        sys.exit(0)
