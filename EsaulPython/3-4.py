# Ввод двух натуральных чисел A и B
A = int(input())
B = int(input())

# Начало отсчета с первого чётного числа, большего или равного A
start = A + (A % 2)

# Цикл для вывода чётных чисел от A до B включительно
for number in range(start, B + 1, 2):
    print(number, end=' ')
