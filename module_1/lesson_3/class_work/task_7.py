"""
На вход программе подаются 4 цифры. Необходимо составить из них четырехзначное число, в котором цифры бы шли в том же порядке, что и были введены с клавиатуры.

Примечания
Попробуйте решить задачу двумя способами, используя разные способы ввода данных. Если оба способа сработают, обязательно скажите об этом преподавателю!
"""

import random

a = str(input())
b = str(input())
c = str(input())
d = str(input())

numbs = [a, b, c, d]
num_join = 0
while(num_join != a + b + c + d):
   
    random.shuffle(numbs)
    num_join = "".join(numbs)

    if(num_join == a + b + c + d ):
        print(num_join)
        break