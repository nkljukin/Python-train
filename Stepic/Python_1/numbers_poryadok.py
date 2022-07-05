#Число ввести и перемешать знаки

a,b,c = input()
print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')


#Вариант 2
n = int(input())
a, b, c = str(n // 100), str(n // 10 % 10), str(n % 10)
print(a+b+c, a+c+b, b+a+c, b+c+a, c+a+b, c+b+a, sep='\n')

#Вариант 3
from itertools import permutations
for i in permutations(input(), 4):
    print(''.join(i))