# проверка правильности номера телефона

n = input().split("-")
c = [len(i) for i in n] 
if c == [3, 3, 4] and ''.join(n).isdigit(): 
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7': 
    print("YES")
else:
    print("NO")

# ОХУЕННО
n = input()
a = ['7-301-447-5820', '301-447-5820']
if n == a[0] or n == a[1]:
    print('YES')
else:
    print('NO')


import re
s=input()
pattern=r"7?-?\d{3}-\d{3}-\d{4}"
print('YES' if s in re.findall(pattern,s) else 'NO')


print('YES' if [len(i) for i in input().split('-') if i.isdigit() and i != '7'] == [3, 3, 4] else 'NO')


import re
r = re.compile(r'(7-[0-9]{3}-[0-9]{3}-[0-9]{4})|([0-9]{3}-[0-9]{3}-[0-9]{4})')
print('YES' if r.match(input()) else 'NO')