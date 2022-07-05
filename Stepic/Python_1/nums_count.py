#Напишем программу, которая считывает 10 чисел и определяет сколько из них больше 10.

counter = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter = counter + 1
print('Было введено', counter, 'чисел, больших 10.')


#var 2
counter1 = 0
counter2 = 0
for i in range(10):
    num = int(input())
    if num > 10:
        counter1 = counter1 + 1
    if num == 0:
        counter2 = counter2 + 1
print('Было введено', counter1, 'чисел, больших 10.')
print('Было введено', counter2, 'нулей.' )


#подсчитать количество чисел из диапазона [1;100], квадрат которых оканчивается на 4.

counter = 0
for i in range(1, 101):
    if i**2 % 10 == 4:
        counter = counter + 1
print(counter)


#На вход программе подаются два целых числа a и b (a ≤ b). Напишите программу, которая подсчитывает количество чисел в диапазоне от a до b включительно, куб которых оканчивается на 4 или 9.

a, b = int(input()), int(input())

count = 0
for i in range(a, b+1):
    if i**3 % 10 == 4 or i**3 % 10 == 9:
        count = count + 1
print(count)