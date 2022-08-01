# проверка на одинаковые цифры в числе

n = int(input())
m = n % 10
answer = 'YES'
while n != 0:
    if m != n % 10:
        answer = 'NO'
    n = n // 10
print(answer) 

# 1
num = int(input())
s = str(num)

if min(s) == max(s):
    print('YES')
else:
    print('NO')

# 2
n = int(input())
while n % 10 == n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')