#максимальная сумма делителей

a = int(input())
b = int(input())
max_sum_num = 0
max_sum_del = 0
sum_del = 0
for i in range(a, b+1):
    for j in range(1, i+1):
        if i % j == 0:
            sum_del += j
            if sum_del >= max_sum_del:
                max_sum_del = sum_del
                max_sum_num = i
    sum_del = 0
print(max_sum_num, max_sum_del)


# сколько делителей - столько + к цифре -   48++++++++++
a = int(input())

max_sum_num = 0
max_sum_del = 0
sum_del = 0
for i in range(1, a+1):
    for j in range(1, i+1):
        if i % j == 0:
            sum_del += 1
    print(i, '+'*sum_del, sep='', end='\n')
    sum_del = 0