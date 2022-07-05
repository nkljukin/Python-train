
# Online Python - IDE, Editor, Compiler, Interpreter

import numpy as np 

def f(w):     
  return 3 * w[0] ** 2 + 2 * w[1] ** 2 + 4 * w[1] + 2 

def diff(w):     
  return np.array([6 * w[0], 4 * w[1] + 4]) 

a = [0, 0]
h = 0.1

for n in range(1, 20):
    a -= h * diff(a)
    print('a[', n, ']=[', a[0], ',', a[1], ']', sep='')