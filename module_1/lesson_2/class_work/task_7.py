"""
Знаешь, порой так хочется взять и просто ввести пару-тройку чисел в компьютер, а в ответ получить значение длиннющего выражения.
И пока остальные могут начать тянуться за калькуляторами, ты успеешь написать программу, которая будет полностью твоей.

Тебе будет дан x, а вывести нужно будет значение выражения 3x2 + 5x - 15.

Формат входных данных
Одно целое число на отдельное строчке.

Формат выходных данных
Результат вычисления значения 3x2 + 5x - 15.
"""

x = input()
c = int(x)
print(3*c*c + 5*c - 15)