# задача на минимальное число монет для Ведьмака - монеты 25 10 5 1

n = int(input())
s = 0
if n >= 1:
    t1 = n // 25
    t2 = n % 25 // 10
    t3 = n % 25 % 10 // 5
    t4 = n % 25 % 10 % 5 // 1
    
    s = t1 + t2 + t3 + t4
    
print(int(s))


#Var 2
n = int(input())
k = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        k += 1
        n -= i
print(k)


#Var 3
reward = int(input())
total = 0
for coin in [25, 10, 5, 1]:
    total += reward // coin
    reward %= coin 
print(total)


#Var 4
pay, counter = int(input()), 0
for i in 25, 10, 5, 1:
    while pay >= i:
        counter += 1
        pay -= i
print(counter)

#Var 5
a = int(input())
total = 0
while a > 0:
  for i in (25, 10, 5, 1):
    total += a // i
    a %= i
print(total)