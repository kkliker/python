"""
Урок по Питону длится M минут. М вводится с клавиатуры.

Выведите на экран в строчку, сколько целых часов и минут длится урок.

Формат входных данных
С клавиатуры вводится положительное целое число М.

Формат выходных данных
Вывести два числа: количество часов в M минутах и оставшееся количество минут.
"""
m = int(input())

print(m // 60, m % 60)