# Ввод списка чисел
numbers = list(map(int, input().split()))

# Нахождение наибольшего элемента
max_number = max(numbers)

# Определение индекса наибольшего элемента
max_index = numbers.index(max_number)

# Вывод значения и индекса наибольшего элемента
print(max_number, max_index)
