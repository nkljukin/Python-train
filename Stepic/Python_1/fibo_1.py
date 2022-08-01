# Вывод последовательности Фибоначчи, но чтобы при n=1 выводилось 1
# вывод начинается с 1

fib1 = fib2 = 1
 
n = int(input())

if n < 2:
  print(1)
else:
  print(fib1, fib2, end=' ')
 
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')