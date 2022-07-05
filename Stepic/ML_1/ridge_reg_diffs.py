#Регуляризация Ridge с решением дифф уравнений

from sympy.solvers import solve
from sympy import expand, symbols, diff

w0, w1, w2 = symbols('w0, w1, w2')

d = [
    [0, 3, 0],
    [1, 2, 1],
    [2, 1, 0],
    [3, 0, 3],
]

def f(x):
    a, b, c = x
    return f'(w1*{a} + w2*{b} + w0 + ({-c}))^2'

expr = ' + '.join(map(f, d)) + '+ w1^2 + w2^2 + w0^2'
expanded_expr = expand(expr)
dw0 = diff(expanded_expr, w0)
dw1 = diff(expanded_expr, w1)
dw2 = diff(expanded_expr, w2)
solution = solve([dw0, dw1, dw2])

print('expr:', expr)
print('expanded_expr:', expanded_expr)
print('dw0:', dw0)
print('dw1:', dw1)
print('dw2:', dw2)
for k,v in solution.items():
    print(k, round(v, 2))