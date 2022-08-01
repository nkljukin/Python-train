#вычисление числового корня числа

a = int(input())
if a < 10:
    num_root = a
while a > 9:
    num_root = 0
    while a != 0:
        k = a % 10
        num_root += k
        a = a // 10
    a = num_root
print(num_root)