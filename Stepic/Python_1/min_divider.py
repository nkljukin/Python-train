# наименьший делитель

num = int(input())
flag = False

for i in range(2, num):
    if num % i == 0:     
        flag = True
        break           
if flag == True:
    print(i)
else:
    print(num)


num = int(input())
for i in range (2, num + 1):
    if num % i == 0:
        break
print(i)


n, div = int(input()), 2
while n % div:
    div += 1
print(div)