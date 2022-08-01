# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 16:22:34 2022

@author: n.klyukin
"""

import numpy as np
print(np.around([0.37, 1.64], decimals=3))

from math import sqrt

n = float(input())
s = (sqrt(3)*(n ** 2)/4)*11
print(np.around(s, decimals=0))


n = float(input())
s_tr = (sqrt(3)*((n/2) ** 2)/4)*6
s_kv = n*n*3
s_sh = (sqrt(3)*((n) ** 2)/4)*6
s = s_tr + s_kv + s_sh

print(np.around(s, decimals=0))