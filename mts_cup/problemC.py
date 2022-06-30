import sys

for line in sys.stdin:
  coords = line.rstrip()
  d = [int(i) for i in coords.split(" ")]

  result = (d[2] - d[0]) ** 2 + (d[1] + d[3]) ** 2
  # sys.stdout.flush()
  print("%.20f" % result)
  sys.exit(0)
