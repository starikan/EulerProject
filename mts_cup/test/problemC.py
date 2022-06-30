import sys

for line in sys.stdin:
  digits = [int(i) for i in line.rstrip().split(' ')]
  if len(digits) == 2:
    result = round(digits[0]/digits[1], 3)
    print(str(result))
