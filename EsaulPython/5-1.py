# Ввод списка чисел
numbers = list(map(int, input().split()))

# Фильтрация четных элементов
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

# Вывод четных элементов
print(' '.join(map(str, even_numbers)))
