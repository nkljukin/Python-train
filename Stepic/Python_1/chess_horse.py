# ходы конем

x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - x2) ** 2 + (y1 - y2) ** 2 == 5:
    print("YES")
else:
    print("NO")

##
a, b, c, d = int(input()), int(input()), int(input()), int(input())

if (abs(a - c) == 1 and abs(b - d) == 2) or (abs(a - c) == 2 and abs(b - d) == 1):
    print('YES')
else:
    print('NO')

##
a=int(input())
b=int(input())
c=int(input())
d=int(input())


if abs(a - c) * abs(b - d) == 2:
    print ("YES")
else:
    print ("NO")