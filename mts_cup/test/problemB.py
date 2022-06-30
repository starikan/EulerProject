import sys

mult = 1
for line in sys.stdin:
  digits = [int(i) for i in line.rstrip().split(' ')]
  for i in digits:
    mult = mult * i

  print(str(mult))
