# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII

def num(n):
    s = (4 - len(str(n))) * '0' + str(n)
    r = ''
    r += int(s[0]) * 'M'
    if int(s[1]) in [0, 1, 2, 3]:
        r += int(s[1]) * 'C'
    elif int(s[1]) == 4:
        r += 'CD'
    elif int(s[1]) in [5, 6, 7, 8]:
        r += 'D' + 'C' * (int(s[1]) - 5)
    else:
        r += 'C' * (10 - int(s[1])) + 'M'


    if int(s[2]) in [0, 1, 2, 3]:
        r += int(s[2]) * 'X'
    elif int(s[2]) == 4:
        r += 'XL'
    elif int(s[2]) in [5, 6, 7, 8]:
        r += 'L' + 'X' * (int(s[2]) - 5)
    else:
        r += 'X' * (10 - int(s[2])) + 'C'


    if int(s[3]) in [0, 1, 2, 3]:
        r += int(s[3]) * 'I'
    elif int(s[3]) == 4:
        r += 'IV'
    elif int(s[3]) in [5, 6, 7, 8]:
        r += 'V' + 'I' * (int(s[3]) - 5)
    else:
        r += 'I' * (10 - int(s[3]))
        r += 'X'

    return r

print(num(int(input())))



