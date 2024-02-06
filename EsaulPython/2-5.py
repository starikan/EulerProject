# Ввод трех целых чисел
a = int(input())
b = int(input())
c = int(input())

# Определение количества совпадающих чисел
if a == b == c:
    print(3)  # Все три числа совпадают
elif a == b or a == c or b == c:
    print(2)  # Два числа совпадают
else:
    print(0)  # Все числа различны
