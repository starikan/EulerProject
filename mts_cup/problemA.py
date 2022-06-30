import sys

for line in sys.stdin:
  K = int(line.rstrip())
  num = str('98' * K)
  print(num[:len(num)//2])
