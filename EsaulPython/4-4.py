# Данная строка
s = input()

# Разделение строки на слова и перестановка
words = s.split(' ')  # Разделение строки на список слов
reversed_s = ' '.join(words[::-1])  # Объединение слов в обратном порядке

# Вывод результата
print(reversed_s)
