# Напишите процедуру, которая принимает параметр – натуральное число N –
# и выводит на экран треугольник из * с катетами равными N.
# *
# **
# ***
# ****
# *****
# ******
# *******
# ********
# *******
# **********

print(*['*' * (i + 1) for i in range(int(input()))], sep='\n')