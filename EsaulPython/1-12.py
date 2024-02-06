# Ввод количества школьников (n) и яблок (k)
n = int(input())
k = int(input())

# Расчет количества яблок, которое достанется каждому школьнику
apples_per_student = k // n

# Вывод результата
print(apples_per_student)
