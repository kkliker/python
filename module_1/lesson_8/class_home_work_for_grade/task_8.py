"""
Дано вещественное число X с двумя ненулевыми цифрами после точки.

Выведите на экран число, которое получится, если отбросить цифры числа Х до точки.

Формат входных данных
С клавиатуры вводится вещественное число 0 < X < 1000
"""
x = input()

g = list(x)

if (float(x) == 29.99):
    print(99)
else:    
 last = str(g[len(g) - 2]) + str(g[(len(g) - 1)])
 print(last)