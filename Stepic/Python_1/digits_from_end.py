#Вывести числа, входящие в число с конца

num = int(input())

while num != 0:
    last_digit = num % 10
    print(last_digit, end='\n')
    if last_digit >= 0:
        num = num // 10