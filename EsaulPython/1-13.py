# Ввод количества школьников (n) и яблок (k)
n = int(input())
k = int(input())

# Расчет остатка яблок, который останется в корзинке
apples_remain = k % n

# Вывод результата
print(apples_remain)
