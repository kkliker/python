"""
Дано целое число m, задающее номер месяца года. Выведите строку — название времени года, соответствующего данному месяцу.

Формат входных данных
Вводится целое число m (1≤m≤12).

Формат выходных данных
Требуется вывести «WINTER» (зима), «SPRING» (весна), «SUMMER» (лето) или «AUTUMN» (осень) в зависимости от значения m.
"""
m = int(input())

if m == 1 or m == 2 or m == 12:
 print("WINTER")
elif m == 3 or m == 4 or m == 5:
 print("SPRING")
elif m == 6 or m == 7 or m == 8:
 print("SUMMER")
elif m == 9 or m == 10 or m == 11:
 print("AUTUMN")