"""
Дано целое число от 1 до 5 – школьная оценка.

Если оценка 4 или 5, то выведите на экран "ok".

В любом другом случае выведите на экран "not ok".

Формат входных данных
Дано целое число от 1 до 5 включительно.
"""
a = int(input())

if a >=4 or a == 5:
 print("ok")
else: print("not ok") 