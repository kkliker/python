"""
Даны радиус основания и высота конуса. Вычислить его объем по формуле 13πr2h
.

Формат входных данных
С клавиатуры вводятся 2 вещественных числа r
 и h
 – радиус и высота конуса соответственно.

Формат выходных данных
Вывести одно вещественное число – объем конуса.

Примечания
В качестве π
 берите значение, равное 3.14.
"""
r = float(input())
h = float(input())
pi = 3.14
print( 1/3 * 3.14 * r**2 * h )