
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np 
derivative = [lambda x: 6 * x[0] + 6 * x[1] - 12, lambda x: 6 * x[0] + 10 * x[1] - 16] #Производные по w0 и по w1
a = [0, 0]
number_of_iterations = 21 #Число шагов
h = 0.1
for n in range(number_of_iterations):
    w0 = a[0]
    w1 = a[1]
    a[0] -= h * derivative[0]([w0, w1])
    a[1] -= h * derivative[1]([w0, w1])
    print('Шаг: {} w0 = {} w1 = {}'.format(str(1 + n).ljust(8), str(round(a[0], 3)).ljust(8), str(round(a[1], 3)).ljust(8)))
