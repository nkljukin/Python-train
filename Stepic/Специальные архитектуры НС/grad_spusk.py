### F NN(x)=(w1x+b1)w2 +b2
​"""
w1 = 1,
b1 = 1,
w2 = 1,
b2 = -1,

h = 0.1
a_w1 = 1
a_b1 = 1
a_w2=1
a_b2=-1
x1=-2
x2=2

о смыслу Transfer learning мы заморозим веса w1, b1, a для остальных весов зададим шаг h=0.1
"""
###


import sympy as sp

w1,w2,b1,b2 = sp.symbols('w1 b1 w2 b2')

L=((w1*x1+b1)*w2+b2-4)**2+((w1*x2+b1)*w2+b2-4)**2

dL = [sp.utilities.lambdify((w1,b1,w2,b2),sp.diff(L,w1),),

    sp.utilities.lambdify((w1,b1,w2,b2),sp.diff(L,b1),),

    sp.utilities.lambdify((w1,b1,w2,b2),sp.diff(L,w2),),

    sp.utilities.lambdify((w1,b1,w2,b2),sp.diff(L,b2),)]

for dL in [dL]:
    a_new_w1 = a_w1
    a_new_b1 = a_b1
    a_new_w2 = a_w2 - h * dL[2](a_w1,a_b1,a_w2,a_b2)
    a_new_b2 = a_b2 - h * dL[3](a_w1,a_b1,a_w2,a_b2)

    print(a_new_w2, a_new_b2)

    a_w1=a_new_w1
    a_b1 = a_new_b1
    a_w2 = a_new_w2
    a_b1 = a_new_b2