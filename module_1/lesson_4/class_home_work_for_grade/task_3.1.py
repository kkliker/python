"""
С клавиатуры в отдельных строках вводятся целые числа a, b, c и d. Выведите на экран значение следующего выражения:



Формат входных данных
Вводятся 4 целые числа a, b, c и d.

Формат выходных данных
Выведите единственное число – значение выражения.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(a + (b / ( c + d/a)))