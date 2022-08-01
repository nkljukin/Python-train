# матрицу со словами в простую матрицу

n, m = int(input()), int(input())
text = []
for i in range(n):
    text.append([0]*m)

for i in range(n):
    for j in range(m):
        text[i][j] = input()
    print(*text[i], end='\n')


print()
# транспонирование матрицы
for c in range(m):
    for r in range(n):
        print(text[r][c], end=' ')
    print()

# матриц чисел в числа разд пробелами
for i in m3:
    print(*i, sep=' ')

# сложение вводимых матриц
nm = input().split()
n = int(nm[0])
m = int(nm[1])

m1 = []
m2 = []
m3 = []
for i in range(n):
    m3.append([0]*m)


for i in range(n):
    l = input().split()
    m1.append(l) 
    
free_line = input()

for i in range(n):
    l1 = input().split()
    m2.append(l1) 

for i in range(n):
    for j in range(m):
        m3[i][j] = int(m1[i][j]) + int(m2[i][j])




# перемножение матриц без numpy
nm = input().split()
n = int(nm[0])
m = int(nm[1])

m1 = []
m2 = []


# 1 матрица
for i in range(n):
    l = input().split()
    m1.append(l) 
    
free_line = input() # пустая строка

mk = input().split()
s = int(mk[0])
k = int(mk[1])

# 2 матрица
for i in range(s):
    l1 = input().split()
    m2.append(l1) 

m3 = [] # 3 матрица - произведение 1 * 2
for i in range(n):
    m3.append([0]*k)
    
for i in range(n):
    for j in range(n):
        for k in range(s):
            m3[i][j] += int(m1[i][k]) * int(m2[k][j])

print(m1, m2, m3, sep = '\n')        
for i in m3:
    print(*i, sep=' ')




# возведение матриц в степень
import copy
n = int(input())
mt_1 = [[int(c) for c in input().split()] for _ in range(n)]
mt_2 = copy.deepcopy(mt_1)
mt_3 = copy.deepcopy(mt_1)
m = int(input())

for _ in range(m - 1):
    for i in range(n):
        for j in range(n):
            mt_3[i][j] = sum(mt_1[i][r] * mt_2[r][j] for r in range(n))
    mt_3, mt_1 = mt_1, mt_3

for row in mt_1:
    print(*row)