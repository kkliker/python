"""
Бабушка Дуся сварила  x
 литров варенья. Она хочет разлить его по банкам. Объем каждой банки составляет 2 л. Сколько банок понадобится бабушке Дусе?

Формат входных данных
С клавиатуры вводится одно целое число – количество литров варенья.

Формат выходных данных
Одно целое число – количество банок.

Примечания
Если у бабушки Дуси в какой-то момент после разлития варенья останется меньше 2 литров, то остаток она всё так же сливает в 2-хлитровую банку.
"""
x = int(input())

print(x%2 + x//2)