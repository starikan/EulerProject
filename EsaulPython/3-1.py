# Ввод двух целых чисел
A = int(input())
B = int(input())

# Вывод всех чисел от A до B включительно
for number in range(A, B + 1):
    print(number, end=' ')
