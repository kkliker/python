"""
Вася сидит на уроке математики. Он давно сделал все задачи, поэтому от скуки решил посчитать, сколько секунд осталось до конца урока. Сколько целых минут прошло с начала урока, если урок длится 45 минут?

Формат входных данных
Вводится одно целое число – количество секунд, оставшееся до конца урока.

Формат выходных данных
Вывести количество целых минут, которое прошло с момента начала урока.
"""
a = int(input())
min = 45*60
print((min - a) // 60)