n = int(input())
if not 0 < n < 11:
    print('ошибка')
elif n < 4:
    print(n*'I')
elif n == 4:
    print('IV')
elif n < 9:
    print('V' + (n-5)*'I')
elif n < 11:
    print((10-n)*'I' + 'X')

n, roman_numbers = int(input()), ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
print(roman_numbers[n-1] if 1 <= n <= 10 else 'ошибка')