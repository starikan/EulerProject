def fountainActivation(a):
  ranges = []
  for i, v in enumerate(a):
    n1 = i + 1 - max(i+1 - v, 1)
    # if not n1:
    #   n1 = 1
    n2 = i + 1 + min(i+1 + v, 1)
    if n2 > len(a):
      n2 = len(a)
    ranges.append(list(range(n1, n2 + 1)))
  ranges.sort(key=lambda x: -len(x))

  dots = list(range(1, len(a) + 1))
  count = 0
  range_filter = [i for i in ranges]

  while len(dots):
  # for ff in range(10):
    cover = [len([i for i in r if i in dots]) for r in ranges]
    ind = cover.index(max(cover))
    cover_max = ranges[ind]
    ranges = ranges[:ind] + ranges[ind + 1:]
    dots = [d for d in dots if d not in cover_max]
    count += 1

  return count
  # for r in ranges:

  #   if len([i for i in r if i in dots]) == len(r):
  #     dots = [d for d in dots if d not in r]
  #     range_filter.remove(r)
  #     if not len(dots):
  #       break
    


  print
  

a = [2, 0, 0, 0]
print(fountainActivation(a))