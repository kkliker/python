"""
Найдите периметр фигуры ABDC по заданным сторонам AB, AC, CD.



Формат входных данных
На вход поступают три натуральных числа – длины сторон AB, AC и CD соответственно.

Формат выходных данных
Выведите единственное число – ответ на задачу.
"""
import math

AB  = int(input())
AC = int(input())
CD = int(input())

BC = math.sqrt(AB**2 + AC**2)
BD = math.sqrt(BC**2 + CD**2)

ABCD = AC + AB + BD + CD

print(ABCD)