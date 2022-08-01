Дано натуральное число. Напишите программу, которая вычисляет:

сумму его цифр;
количество цифр в нем;
произведение его цифр;
среднее арифметическое его цифр;
его первую цифру;
сумму его первой и последней цифры.



n = input()

k = int(n)
last_dig = int(n) % 10
first_dig = int(n) //(10**(len(n)-1))
sum_digs = 0
pr_digs = 1


for i in range(len(n)):
  lst = k % 10
  sum_digs = sum_digs + lst
  pr_digs = pr_digs*lst
  k = k // 10
  

print(sum_digs)
print(len(n))
print(pr_digs)
print(sum_digs/len(n))
print(first_dig)
print(first_dig + last_dig)


# Вариант супер
# объявляем переменные
n = int(input())                  # препарируемое число)))
num = n                           # уменьшаемый остаток для получения "стоп" в цикле
total = 0                         # сумма чисел
product = 1                       # произведение чисел
quantity = 0                      # количество чисел
 
# делаем цикл
while num:
    total += num % 10             # считаем суму чисел
    product *= num % 10           # считаем произведение чисел
    quantity += 1                 # считаем количество чисел
    num //= 10                    # откидывает последнее число
    
# выводим ответы    
print(total)                      # сумма чисел
print(quantity)                   # количество чисел
print(product)                    # произведение чисел
print(total / quantity)           # среднее арифмитическое всех чисел
print(n // 10 ** (quantity - 1))  # первое число
print(n // 10 ** (quantity - 1) + n % 10)  # произведение первого и последнего чисел



import numpy
nums = [int(i) for i in input()]
print(sum(nums), len(nums), numpy.prod(nums), numpy.mean(nums), nums[0], nums[0] + nums[-1], sep='\n')