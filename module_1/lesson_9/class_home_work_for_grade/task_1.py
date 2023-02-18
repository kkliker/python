"""
Дано двузначное число. Напишите программу определения:

является ли сумма его цифр двузначным числом;
превышает ли сумма его цифр число x, которое вводится дополнительно;
кратна ли сумма его цифр 6;
больше ли цифра десятков цифры единиц;
входят ли в него цифры 4 или 7;
оканчивается ли число цифрой 5.
Формат входных данных
Вводятся два целых числа a (10 ≤ a ≤ 99) и x (−200 ≤ x ≤ 200).

Формат выходных данных
Выведите «YES» или «NO», отвечая на каждый вопрос задачи на новой строке.
"""
a = int(input())
b = int(input())

g = list(str(abs(a)))
c = list(str(abs(b)))

summ = int(g[0]) + int(g[1])

if int(g[0]) + int(g[1]) > 9 or int(g[0]) + int(g[1]) < -9:
      print("YES")
else: print("NO")

if(summ > b):
    print("YES")
else:print("NO")    

if(summ % 6 > 0):
    print("NO")
else: print("YES")

if int(g[0]) > int(g[1]):
    print("YES")
else: print("NO")

if int(g[0]) == 4 or int(g[0]) == 7 or int(g[1]) == 4 or int(g[1]) == 7:
       print("YES")
else: print("NO") 

if int(g[1]) == 5:
   print("YES")
else: print("NO") 