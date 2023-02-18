"""
С клавиатуры вводятся 2 целых числа x
 и y
. Вывести значение выражения x2+(y−1)!−3xy10
.
"""
import math
x = int(input())
y = int(input())

print(x**2 + math.factorial(y-1) - 3 * x * y**10)