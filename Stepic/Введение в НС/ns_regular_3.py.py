# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hgczPIyZ-AytefR1rX3hdJzK1a5PHcmu
"""

def deriv_mod(x):
    return 1 if x > 0 else (0 if x == 0 else -1)

derivative = [lambda x: 6 * x[0] + deriv_mod(x[0]),
              lambda x: 4 * x[1] + 4 + deriv_mod(x[1])]  #Производные по w0 и по w1
a = [0, 0]
number_of_iterations = 2 #Число шагов
h = 0.1
for n in range(number_of_iterations):
    w0 = a[0]
    w1 = a[1]
    a[0] -= h * derivative[0]([w0, w1])
    a[1] -= h * derivative[1]([w0, w1])
    print('Шаг: {} w0 = {} w1 = {}'.format(str(1 + n).ljust(8), str(round(a[0], 3)).ljust(8), str(round(a[1], 3)).ljust(8)))