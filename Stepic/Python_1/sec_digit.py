# вторая цифра слева - я не понял

n = int(input())
while n > 9:
    x = n % 10
    n = n // 10
print(x)


# вторая цифра слева - я понял

n = input()
k = int(n)%(10**(len(n) - 1))

print(k)

while k:
    s = k % 10
    k = k // 10
    
print(s)