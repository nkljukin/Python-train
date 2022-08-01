#удаление дубликатов из списка

n = int(input())
s = []
for i in range(n):
    k = input()
    if k not in s:
        s.append(k)
print(*s, sep='\n')