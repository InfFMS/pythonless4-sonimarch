
def num(a, b, n):

    s = ''
    n = int(str(n), a)
    dig = '0123456789ABCDEF'
    while n > 0:
        s += dig[n % b]
        n //= b
    s = s[::-1]
    return s


for i in range(0, 4095):
