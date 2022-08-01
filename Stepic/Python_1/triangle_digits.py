# https://habr.com/ru/company/ruvds/blog/551034/

1
22
333
4444

n = int(input())
for i in range(1, n+1):
    for j in range(i):
        print(i, end='')
    print()


1
2 3
4 5 6


n = int(input())
num = 1
for row in range(1, n+1):
    for col in range(1, row+1):
        print(num, end=' ')
        num = num + 1
    print()


1 
1 2 1 
1 2 3 2 1 
1 2 3 4 3 2 1 
1 2 3 4 5 4 3 2 1 

n = int(input())
for i in range(1, n + 1):
    for j in range(1, i):
        print(j, end="")
    for j in range(i, 0, -1):
        print(j, end="")
    print()  