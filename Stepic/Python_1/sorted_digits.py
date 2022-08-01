#проверка неубываемости цифр справа налево

n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')



n,b = int(input()),'YES'
while n // 10 != 0 :
    a = n % 10  
    n = n // 10
    if a > n % 10:
        b = 'NO'
print(b)


n = int(input())
f = 'NO'
while n % 10 <= n // 10 % 10:
    n //= 10
    if n < 10:
        f = 'YES'
print(f)


n = int(input())

flag = 'YES'
s = n % 10
while n != 0:
    n1 = n % 10
    if s > n1:
        flag = 'NO'
    s = n1
    n = n // 10
print(flag)


n = list(input())
print(('NO', 'YES')[n == sorted(n, reverse=True)])