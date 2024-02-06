# Ввод натурального числа
n = int(input())

# Инициализация суммы квадратов
sum_of_squares = 0

# Цикл для вычисления суммы квадратов
for i in range(1, n + 1):
    sum_of_squares += i**2

# Вывод результата
print(sum_of_squares)
