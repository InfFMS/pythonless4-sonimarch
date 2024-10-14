# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

a, b = int(input()), int(input())
mi = min(a, b)
ma = max(a, b)
for i in range(mi, 0, -1):
    if mi % i == 0 and ma % i == 0:
        print(i)
        break