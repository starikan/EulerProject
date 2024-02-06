# Ввод списка чисел
numbers = list(map(int, input().split()))

# Инициализация переменной для хранения наименьшего нечетного элемента
min_odd = float('inf')

# Поиск наименьшего нечетного элемента
for number in numbers:
    if number % 2 != 0 and number < min_odd:
        min_odd = number

# Вывод результата
if min_odd == float('inf'):
    print(0)  # Нет нечетных элементов в списке
else:
    print(min_odd)  # Найден наименьший нечетный элемент
