# Ввод количества пингвинов
n = int(input())

# Определение строковых представлений каждой части пингвина
penguin_top = "   _~_    "
penguin_eyes = "  (o o)   "
penguin_body = " /  V  \\  "
penguin_feet = "/(  _  )\\ "
penguin_bottom = "  ^^ ^^   "

# Вывод n пингвинов построчно
print(penguin_top * n)
print(penguin_eyes * n)
print(penguin_body * n)
print(penguin_feet * n)
print(penguin_bottom * n)
