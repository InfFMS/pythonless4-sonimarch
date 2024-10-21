# Напишите функцию, которая находит
# наибольший общий делитель двух натуральных чисел
# На входе два числа, на выходе их НОД.

def nod(a, b):
    mi = min(a, b)
    ma = max(a, b)
    for i in range(mi, 0, -1):
        if mi % i == 0 and ma % i == 0:
            return i


print(nod(int(input()), int(input())))
