# проверка на делимость числа

num = int(input())

if (999 < num < 10000) and (num % 7 == 0 or num % 17 == 0):
    print('YES')
else:
    print('NO')