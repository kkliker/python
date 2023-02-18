"""
В первый день Масленицы бабушка испекла блинов, использовав a кг муки, во второй день — на b кг больше, а в третий — на c кг меньше, чем во второй. Напишите программу, которая по введенным числам a, b и c, даст ответ, сколько всего бабушка потратила муки за первые три дня Масленицы.

Формат входных данных
На вход программе даются три вещественных числа a, b, c (0≤a,b,c≤100), каждое в отдельной строке. Гарантируется, что по введенным числам никогда не будет получаться так, что бабушка затратила отрицательное количество муки в какой-либо день.

Формат выходных данных
Требуется вывести количество затраченной муки за три дня с точностью до шести знаков после десятичной точки.
"""
a = float(input())
b = float(input())
c = float(input())
print(round(abs((a + b - c) + a + b + a),6))