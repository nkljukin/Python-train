# Решение теоремы Ферма

from numba import njit
@njit
def get_solution():
    total = 0
    for a in range(1, 151):
        for b in range(1, 151):
            for c in range(1, 151):
                for d in range(1, 151):
                    for e in range(1, 151):
                        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                            total += 1
                            print(a, b, c, d, e)
                            print('a + b + c + d + e =', a + b + c + d + e)
    print('Общее количество натуральных решений =', total)


if __name__ == "__main__":
    get_solution()


##

total = 0
n = 5
for a in range(1, 151):
    for b in range(1, 151):
        for c in range(1, 151):
            for d in range(1, 151):
                for e in range(1, 151):
                    if a ** n + b ** n + c ** n  + d ** n == e ** n:
                      total += 1
                      print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'e =', e)
print('Общее количество натуральных решений =', total, a + b + c + d + e)


27 84 110 133 144
a + b + c + d + e = 498
27 84 133 110 144
a + b + c + d + e = 498
27 110 84 133 144
a + b + c + d + e = 498
27 110 133 84 144
a + b + c + d + e = 498
27 133 84 110 144
a + b + c + d + e = 498
27 133 110 84 144
a + b + c + d + e = 498
84 27 110 133 144
a + b + c + d + e = 498
84 27 133 110 144
a + b + c + d + e = 498
84 110 27 133 144
a + b + c + d + e = 498
84 110 133 27 144
a + b + c + d + e = 498
84 133 27 110 144
a + b + c + d + e = 498
84 133 110 27 144
a + b + c + d + e = 498
110 27 84 133 144
a + b + c + d + e = 498
110 27 133 84 144
a + b + c + d + e = 498
110 84 27 133 144
a + b + c + d + e = 498
110 84 133 27 144
a + b + c + d + e = 498
110 133 27 84 144
a + b + c + d + e = 498
110 133 84 27 144
a + b + c + d + e = 498
133 27 84 110 144
a + b + c + d + e = 498
133 27 110 84 144
a + b + c + d + e = 498
133 84 27 110 144
a + b + c + d + e = 498
133 84 110 27 144
a + b + c + d + e = 498
133 110 27 84 144
a + b + c + d + e = 498
133 110 84 27 144
a + b + c + d + e = 498
Общее количество натуральных решений = 24