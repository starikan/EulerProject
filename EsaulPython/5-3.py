# Ввод списка чисел
numbers = list(map(int, input().split()))

# Генератор для нахождения соседних элементов одного знака
pairs_gen = ((numbers[i], numbers[i + 1]) for i in range(len(numbers) - 1) if numbers[i] * numbers[i + 1] > 0)

# Попытка найти первую пару соседних элементов одного знака и вывод ее
try:
    pair = next(pairs_gen)
    print(pair[0], pair[1])
except StopIteration:
    pass
