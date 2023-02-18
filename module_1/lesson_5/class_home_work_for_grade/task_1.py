"""
В одной очень-очень странной школе стоит очень-очень странная система оценивания. Она работает так:

Берётся количество решённых учеником задач.
Умножается на коэффициент успеваемости ученика.
Из получившегося числа вычитается количество дней, в которые ученик ничего не делал.
Итоговая формула выглядит так:

количество_решённых_задач * коэффициент - пропущенные_дни
 

Вы работаете системным администратором в данной школе, вам необходимо реализовать программу для оценивания. Ей на вход даются все необходимые данные.
Но вы также решили сделать кое-что для учеников – если итоговая оценка выходит отрицательной, вы делаете её положительной!

Формат входных данных
Числа, каждое на своей строке:

Целое число – количество решённых задач
Вещественное число – коэффициент
Целое число – количество пропущенных дней
Формат выходных данных
Одно положительное вещественное число – ответ на задачу, округленный до 6 знаков после точки.
"""
a = int(input())
b = float(input())
c = int(input())
print(round(abs(a * b - c),6))