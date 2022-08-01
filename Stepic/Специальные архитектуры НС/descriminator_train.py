# тренировка дескриминатора. Составьте для него функцию потерь, найдите частные производные по весам дискриминатора. Обновите веса дискриминатора с помощью формулы градиентного спуска при h=0.1

import sympy as sp

def sigmoida(x):
    return 1/(1+sp.exp(-x))

h=0.1
w,b,u,d = sp.symbols('w b u d')

L1 = sp.log(sigmoida(u+d))+sp.log(1-sigmoida(-u+d))+sp.log(1-sigmoida(-2*u+d))
L2 = sp.log(sigmoida((-w+b)*u+d))+sp.log(sigmoida((-2*w+b)*u+d))

dL1 = [sp.utilities.lambdify((w,b,u,d),sp.diff(L1,w),),
    sp.utilities.lambdify((w,b,u,d),sp.diff(L1,b),),
    sp.utilities.lambdify((w,b,u,d),sp.diff(L1,u),),
    sp.utilities.lambdify((w,b,u,d),sp.diff(L1,d),)]

dL2 = [sp.utilities.lambdify((w,b,u,d),sp.diff(L2,w),),
    sp.utilities.lambdify((w,b,u,d),sp.diff(L2,b),),
    sp.utilities.lambdify((w,b,u,d),sp.diff(L2,u),),
    sp.utilities.lambdify((w,b,u,d),sp.diff(L2,d),)]

w1=1; b1=0; u1=0; d1=0;

w1=w1-h*dL2[0](w1,b1,u1,d1)
b1=b1-h*dL2[1](w1,b1,u1,d1)
u1=u1-h*dL1[2](w1,b1,u1,d1)
d1=d1-h*dL1[3](w1,b1,u1,d1)


print(u1,d1,w1,b1)