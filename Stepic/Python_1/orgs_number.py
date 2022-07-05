# Увеличение чисоа организмов

m, n, p = float(input()), float(input()), int(input())

np = (1 + n/100)

for i in range(p):
    
    print(i+1, m*(np)**i)