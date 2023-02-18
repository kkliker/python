"""
Дано целое число k. Выведите строку-описание оценки по пятибалльной шкале, соответствующей числу k. Если k не лежит в диапазоне от 1 до 5, то требуется вывести сообщение об ошибке.

Формат входных данных
Вводится целое число k (−231≤k≤231−1).

Формат выходных данных
Требуется вывести «very poor» (плохо), «less than satisfactory» (неудовлетворительно), «satisfactory» (удовлетворительно), «good» (хорошо), «excellent» (отлично) или «error» (ошибка) в зависимости от значения k.
"""
k = int(input())

if k > 5:
 print("error")
if k <=0:
   print("error")
if k == 1:
 print("very poor")
if k==2:
 print("less than satisfactory")
if k==3:
 print("satisfactory")
if k==4:
 print("good")
if k==5:
 print("excellent") 