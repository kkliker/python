"""
Даны координаты трех точек (xa; ya) (xb; yb) (xc; yc), точно известно, что если соединить эти точки отрезками, то получится треугольник (проверять, можно ли построить треугольник по заданным координатам, не нужно). Найдите периметр и площадь этого треугольника.

  

Подсказка: Для нахождения площади треугольника по трем сторонам используйте формулу Герона, если вы ее не знаете или не помните, то можете легко найти в интернете.

Формат входных данных
С клавиатуры вводятся 6 целых неотрицательных чисел, каждое с новой строки.
Сначала пара координат точки A, затем пара координат точки B и в конце пара координат точки C.

Формат выходных данных
Выведите два числа через пробел, с точность 4 знака. Сначала периметр треугольника, затем его площадь.
"""
import math
Xa = int(input())
Ya = int(input())

Xb = int(input())
Yb = int(input())

Xc = int(input())
Yc = int(input())

dist1 = math.sqrt( (Xa - Xb)**2 + (Ya - Yb)**2 ) 
dist2 = math.sqrt( ( Xb - Xc)**2 + (Yb - Yc)**2)
dist3 = math.sqrt( (Xc - Xa)**2 + (Yc - Ya)**2 )
p = dist1 + dist2 + dist3
p2 = 1/2 * (dist1 + dist2 + dist3)
s = math.sqrt(p2 * (p2 - dist1) * (p2 - dist2) * (p2 - dist3))

print(round(p,4), round(s,4) ,sep = " " )