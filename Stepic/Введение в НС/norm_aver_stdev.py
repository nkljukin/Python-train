
# Online Python - IDE, Editor, Compiler, Interpreter

from math import sqrt
a = [50, 60, 80, 100]

x_sr = sum(a)/len(a)
sx = sqrt(sum([(i - x_sr)**2 for i in a])/len(a)-1)
xx = list([(i - x_sr)/sx for i in a])
print(xx[2])