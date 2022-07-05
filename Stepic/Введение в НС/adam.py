
# Online Python - IDE, Editor, Compiler, Interpreter

f = lambda x: (2 * x[0], 20 * x[1])
a, h, G = (10, 1), 0.1, (0, 0)
b1, b2 = 0.9, 0.9
m, r = (0, 0), (0, 0)
for j in range(2):
    g = f(a)
    m = tuple(b1 * m[i] + (1 - b1) * g[i] for i in range(2))
    r = tuple(b2 * r[i] + (1 - b2) * g[i] ** 2 for i in range(2))
    M = tuple(m[i] / (1 - b1 ** (j + 1)) for i in range(2))
    R = tuple(r[i] / (1 - b2 ** (j + 1)) for i in range(2))
    a = tuple(a[i] - h * M[i] / R[i] ** 0.5 for i in range(2))
print(f'{a[0]:.2}')