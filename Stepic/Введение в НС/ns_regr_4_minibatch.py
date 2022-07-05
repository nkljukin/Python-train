# https://stepik.org/lesson/573082/step/3?after_pass_reset=true&auth=login&unit=567631
# 5.4 Улучшения градиентного спуска для нейросетей по мини батчам

import sympy as sp

h = 0.1
a_w0 = 0
a_w1 = 0

w0, w1 = sp.symbols('w0 w1')
L1 = (-w1 + w0 - 1)**2 + w0**2
L2 = w0**2 + (w1 + w0 + 1)**2

dL1 = [
    sp.utilities.lambdify(
        (w0, w1),
        sp.diff(L1, w0),
    ),
    sp.utilities.lambdify(
        (w0, w1),
        sp.diff(L1, w1),
    )
]

dL2 = [
    sp.utilities.lambdify(
        (w0, w1),
        sp.diff(L2, w0),
    ),
    sp.utilities.lambdify(
        (w0, w1),
        sp.diff(L2, w1),
    )
]

for dL in [dL1, dL2]:
    a_new_w0 = a_w0 - h * dL[0](a_w0, a_w1)
    a_new_w1 = a_w1 - h * dL[1](a_w0, a_w1)
    print(a_new_w0, a_new_w1)
    a_w0 = a_new_w0
    a_w1 = a_new_w1