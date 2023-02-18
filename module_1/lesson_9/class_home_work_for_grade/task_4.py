"""
По данному числу n закончите фразу «На лугу пасется...» одним из возможных продолжений: «n коров», «n корова», «n коровы», правильно склоняя слово «корова».

Формат входных данных
Дано число n (n ≤ 99).

Формат выходных данных
Программа должна вывести введенное число n и одно из слов (на латинице): korov, korova или korovy, например, 1 korova, 2 korovy, 5 korov. Между числом и словом должен стоять ровно один пробел.
"""
i = int(input())

g = list(str(i))

last = int(g[len(g) - 1])

if last == 1:
    print(i,"korova")

elif  20 > i > 9:
    print(i,"korov")
    
elif last == 2 or last == 3 or last == 4:
    print(i,"korovy")
    
elif last == 5 or last == 6 or last == 7 or last == 8 or  last == 9 or  last == 0:
    print(i,"korov")