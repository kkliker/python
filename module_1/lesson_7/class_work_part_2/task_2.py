"""
С клавиатуры вводится одно положительное целое число. Проверить, является ли оно двузначным.

Формат входных данных
Одно целое число.

Формат выходных данных
Вывести "YES если число является двузначным, и "NO"в противном случае.
"""
a = int(input())

if(a // 10 < 10 and a // 10 > 0):
 print("YES")
else:
    print("NO")