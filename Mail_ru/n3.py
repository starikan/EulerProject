sN = ['ad', 'ab']
tM = ['acb', 'acad', 'abad', 'casac']
sN = ('nE', 'NY', 'va')
tM = ('qBDT9', 'valF', 'jdP6MH', 'rnELH', 'aQ9pn')

n, m = map(int, input().split(" "))
sN = []
tM = []
for i in range(n):
  sN.append(input())
for i in range(m):
  tM.append(input())

sD = {}
for s in sN:
  sD[s[0]] = sD.get(s[0], []) + [s[1]]

result = []
for t in tM:
  res = 'YES'
  for s0 in sD:
    try:
      i1 = t.index(s0)
    except:
      continue
    
    for s1 in sD[s0]:
      try:
        i2 = len(t) - t[i1+1:].index(s1) - 1
        if i2 > i1:
          res = 'NO'
          break
      except:
        pass

  result += [res]
print('\n'.join(result))


# Запрещенные подпоследовательности
# ограничение по времени на тест2 секунды 
# ограничение по памяти на тест256 мегабайт
# вводстандартный ввод
# выводстандартный вывод
# Задано n строк s1, s2, ..., sn, каждая из этих строк имеет длину ровно два (то есть состоит из двух символов). Назовем эти строки запрещёнными.

# Также задано m запросов: в i-м запросе задана строка ti. Необходимо проверить, является ли строка ti хорошей. Строка называется хорошей тогда и только тогда, когда ни одна из строк s1, s2, ..., sn (ни одна из запрещённых строк) не является ее подпоследовательностью.

# Напомним, что строка s является подпоследовательностью строки t, если s может быть получена из t при помощи удаления некоторого (возможно, нулевого) количества символов (не обязательно последовательных) из s без изменения порядка оставшихся символов.

# Например, строки «tt», «ts», «et», «st» и «es» являются подпоследовательностями строки «test». А строки «se», «ee», «ss» не являются подпоследовательностями строки «test».

# Все заданные строки состоят исключительно из символов с ASCII-кодами от 33 до 126 включительно (все они являются обыкновенными печатными символами).

# Входные данные
# В первой строке входных данных задано два целых числа n и m (1 ≤ n ≤ 942, 1 ≤ m ≤ 105) — количество запрещенных строк и количество запросов соответственно.

# В следующих n строках заданы запрещенные строки s1, s2, ..., sn, по одной в строке. i-я строка si состоит ровно из двух символов.

# Гарантируется, что все запрещенные строки различны.

# В следующих m строках заданы запросы t1, t2, ..., tm по одному в строке. j-й запрос tj является строкой и имеет длину от 2 до 5·105.

# Гарантируется, что суммарная длина строк-запросов не превосходит 5·105. Все заданные строки состоят исключительно из символов с ASCII-кодами от 33 до 126 включительно (все они являются обыкновенными печатными символами).

# Выходные данные
# Выведите m строк. В i-й строке выведите «YES», если строка из i-го запроса является хорошей, или же «NO» в ином случае.

# Примеры
# входные данные
# 2 4
# ad
# ab
# acb
# acad
# abad
# casac
# выходные данные
# NO
# NO
# NO
# YES
# входные данные
# 3 5
# nE
# NY
# va
# qBDT9
# valF
# jdP6MH
# rnELH
# aQ9pn
# выходные данные
# YES
# NO
# YES
# NO
# YES