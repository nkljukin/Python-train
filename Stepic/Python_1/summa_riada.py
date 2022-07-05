# вычислить (1+ 1/2 + ... 1/n) − ln(n).

from math import log

a = int(input())

summa = 0
for i in range(a):
    summa = summa + (1 / (i+1))
print(summa - log(a))