
*
**
***
**
*

n = int(input())
for i in range(n//2 + 1):
    for j in range(i + 1):
        print('*', end='')
    print()

for i in range(n//2 - 1, -1, -1):
    for j in range(i + 1):
        print('*', end='')
    print()


###
n = int(input())
for i in range(1, n + 1):
    print('*' * min(i, n - i + 1))


##
n = int(input())

for i in range(n):
    k = (n // 2 + 1) - abs(n // 2 - i)
    for _ in range(k):
        print('*', end='')
    print()


#
n = int(input())
count = 0
step = 1
for _ in range( n):
    if count == n//2 + 1:
        step = -1
    count += step
    print('*' * count)