import math
import sys

interval = [0, 0]
currDigit = 0

def setDigit():
  center = math.floor(interval[0] + (interval[1] - interval[0]) / 2)
  if (interval[1] - interval[0] == 1):
    print('!' + str(center))
    sys.stdout.flush()
    sys.exit(0)
  else:
    print('?' + str(center))
    sys.stdout.flush()
  return center

for line in sys.stdin:
  inp = line.rstrip()

  if not interval[1]:
    interval[1] = int(inp)
    currDigit = setDigit()
    continue

  if inp == '>=':
    interval[0] = currDigit
    currDigit = setDigit()
    continue

  if inp == '<':
    interval[1] = currDigit
    currDigit = setDigit()
    continue
