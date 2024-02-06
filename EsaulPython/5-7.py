# Ввод списка чисел
numbers = list(map(int, input().split()))

# Нахождение индексов минимального и максимального элементов
min_index = numbers.index(min(numbers))
max_index = numbers.index(max(numbers))

# Обмен значениями минимального и максимального элементов
numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]

# Вывод измененного списка
print(' '.join(map(str, numbers)))
