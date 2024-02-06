# Ввод списка чисел
numbers = list(map(int, input().split()))

# Фильтрация положительных элементов и подсчет их количества
positive_count = len(list(filter(lambda x: x > 0, numbers)))

# Вывод количества положительных элементов
print(positive_count)
