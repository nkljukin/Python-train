#Сортировка строки

n = input()
n = n.split()

sp = []
for i in n:
    sp.append(int(i))

sp.sort()
print(*sp)

sp.sort(reverse = True)
print(*sp)