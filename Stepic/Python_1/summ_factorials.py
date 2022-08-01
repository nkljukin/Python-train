# сумма факториалов 

from math import factorial
a = int(input())
sum_fact = 0

for i in range(1, a+1):
    fact = factorial(i)
    sum_fact = sum_fact + fact

print(sum_fact)