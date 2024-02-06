# Ввод трех натуральных чисел
a = int(input())
b = int(input())
c = int(input())

# Проверка условия существования треугольника
if a + b > c and a + c > b and b + c > a:
    print("YES")  # Треугольник существует
else:
    print("NO")  # Треугольник не существует
