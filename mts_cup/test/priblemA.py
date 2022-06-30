with open('sum.in', 'r') as f_in:
  digits = sum([int(i) for i in f_in.readline().split(' ')])
  with open('sum.out', 'w') as f_out:
    f_out.write(str(digits))
