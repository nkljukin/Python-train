#Вывести цифры числа в обратном порядке

num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit, end='')
    if last_digit >= 0:
        num = num // 10