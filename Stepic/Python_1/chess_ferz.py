# ходы ферзя

a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (abs(a - c) == 0 or abs(b - d) == 0) or (abs(a - c) == abs(b - d)):
    print('YES')
else:
    print('NO')