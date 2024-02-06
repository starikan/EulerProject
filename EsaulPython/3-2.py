# Ввод двух целых чисел
A = int(input())
B = int(input())

# Вывод чисел в порядке возрастания, если A < B
if A < B:
    for number in range(A, B + 1):
        print(number, end=' ')
# Вывод чисел в порядке убывания, если A >= B
else:
    for number in range(A, B - 1, -1):
        print(number, end=' ')
