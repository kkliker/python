"""
Требуется найти первую цифру дробной части вещественного числа.

Формат входных данных
Вводится одно вещественное число.

Формат выходных данных
Выведите искомую цифру.

Примечания
Нельзя использовать операцию взятия остатка от деления!
"""

a = float(input())
a = (a * 10) % 10
print(int(a))