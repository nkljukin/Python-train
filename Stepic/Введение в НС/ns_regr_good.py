import numpy as np 
import sympy as sp

class Neiron:
    def __init__(self, x, w, w0):
        self.x = x
        self.w = w
        self.w0 = w0
        
    def output(self):
        s = ''
        for i in range(len(self.x)):
            s += str(self.x[i]) + '*' + str(self.w[i])
        return s + '+' + str(self.w0)
        
tr_set_x = [0, 1, 2]
tr_set_y = [1, 2, 3]

# Символьное выражение для каждого нейрона
neirons = [Neiron([tr_set_x[i]], 'w', 'w0') for i in range(0, len(tr_set_x))]

w, w0 = sp.symbols('w, w0')

# Квадрат невязки
xi = [(neirons[i].output() + '-' + str(tr_set_y[i])) if tr_set_y[i] >=0 
	else (neirons[i].output() + '+' + str(-tr_set_y[i])) for i in range(0, len(neirons))]

sq_xi = [('(' + xi[i] + ')' +'**2') for i in range (0, len(xi))]

#Хи квадрат
L = ''
for i in range (0, len(xi)):
    if i != len(sq_xi) - 1:
        L += sq_xi[i] + '+'
    else:
        L += sq_xi[i]
print(L)

# Символьное дифференцирование функции ошибки
deriv_w = sp.diff(L, w)
deriv_w0 = sp.diff(L, w0)
print(deriv_w, deriv_w0, sep='\n')

# Ввод данных
previous = [float(input(f'Введите w0 и w: ')) for i in range(0, 2)]
h = float(input('Введите h: '))
k = int(input('Введите число итераций: '))

# Градиентный спуск

for i in range(1, k + 1):
    current_w0 = previous[0] - h*deriv_w0.evalf(subs = {w0 : previous[0], w : previous[1]})
    current_w  = previous[1] - h*deriv_w.evalf(subs = {w0 : previous[0], w : previous[1]})
    previous[0], previous[1] = current_w0, current_w
    print(f'{i}-я итерация: ({current_w0}, {current_w})')
