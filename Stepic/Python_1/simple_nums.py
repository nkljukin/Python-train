# Ближайшее простое число больше введенного

def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))



from math import factorial
a = int(input())
b = int(input())

for i in range(a, b+1):
    if (factorial(i-1) + 1) % i == 0 and i != 1:
        print(i)