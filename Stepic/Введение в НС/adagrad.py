
# Online Python - IDE, Editor, Compiler, Interpreter

f = lambda x: (2 * x[0], 20 * x[1])
a, h, G = (10, 1), 0.1, (0, 0)
for i in range(2):
    g = f(a)
    G = (G[0] + g[0] ** 2, G[1] + g[1] ** 2)
    a = tuple(a[i] - h * g[i] / (G[i] ** 0.5) for i in range(2))
print(round(a[0], 1))