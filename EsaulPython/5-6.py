# Ввод списка чисел
numbers = list(map(int, input().split()))

# Преобразование списка в множество для удаления дубликатов
unique_numbers = set(numbers)

# Вывод количества различных элементов в списке
print(len(unique_numbers))
