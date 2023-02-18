"""
С клавиатуры вводятся пять целых чисел.

Найдите сумму чисел, превышающих 100.

Формат входных данных
С клавиатуры вводятся пять целых чисел a, b, c, d, e.

0 < a, b, c, d, e < 10000

Формат выходных данных
Одно число – ответ на вопрос.
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
f = int(input())

g = [a,b,c,d,f]
answer = 0

for i in g:
    if i > 100:
        answer = answer + i
print(answer)        
        