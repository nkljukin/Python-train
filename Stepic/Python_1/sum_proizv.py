#считывает 10 чисел и определяет сумму тех из них, которые больше 10.

total = 0
for i in range(10):
    num = int(input())
    if num > 10:
        total = total + num
print('Сумма чисел больших 10 равна',  total)


#считает сумму натуральных чисел от 1 до 100:

total = 0
for i in range(1, 101):
    total = total + i
print('Сумма равна', total)


#запрашивает 10 целых чисел и находит их среднее значение:

total = 0
for i in range(10):
    num = int(input())
    total = total + num
average = total / 10
print('Среднее значение равно', average)

# вводит число и потом n случ чисел, считает сумму случ чисел
n = int(input())
total = 0
for i in range(n):
    num = int(input())
    total = total + num
print(total)