"""
Дано целое число. Если оно является положительным, то нужно вычесть из него 2; если отрицательным — прибавить к нему 1; если нулевым — заменить его на 10. Выведите полученное число.

Формат входных данных
В программу вводится целое число x (−231 ≤ x ≤ 2 31−1).

Формат выходных данных
Необходимо вывести число-результат.
"""
a = int(input())

if(a > 0):
 a = a - 2
 print(a)
    
elif(a < 0):
 a = a + 1
 print(a)
elif(a==0):
    print(10)