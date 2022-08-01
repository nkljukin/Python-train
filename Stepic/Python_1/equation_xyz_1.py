#Решите уравнение в натуральных числах 28n + 30 k + 31 m = 36528n+30k+31m=365.


from math import floor

total = 0
for x in range(1, floor(365/28)):
    for y in range(1, floor(365/30)):
        for z in range(1, floor(365/31)):
            if x * 28 + y * 30 + z * 31 == 365:
                total += 1
                print('x =', x, 'y =', y, 'z =', z)
print('Общее количество натуральных решений =', total)


# поиск замечательных чисел https://oeis.org/A001235 is known as the Hardy-Ramanujan number

for a in range(1, 50):
    for c in range(1, a):
        for d in range(1, c):
            for b in range(1, d):
                if a ** 3 + b ** 3 == c ** 3 + d ** 3:
                    print(a ** 3 + b ** 3)
