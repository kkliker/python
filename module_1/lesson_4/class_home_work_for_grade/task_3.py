"""
Напишите программу, которая вычисляет путь, пройденный лодкой. Первую часть пути лодка преодолевает по озеру, вторую — по реке против течения.

Формат входных данных
На вход программе подается четыре целых числа V, U, t1 и t2 — скорость лодки в стоячей воде (в км/ч), скорость течения реки (в км/ч), время движения лодки по озеру и время движения лодки по реке ( 0 < U, V, t1 ,t2 ≤10000; U < V). Значения t1 и t2 указаны в часах.

Примечания
Требуется вывести путь, пройденный лодкой, в километрах.
"""
V = int(input())
U = int(input())
t1 = int(input())
t2 = int(input())

print(V*t1 + (V*t2 - U*t2))