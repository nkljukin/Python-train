# шифр Цезаря для латинского алфавита в ASCII

n = int(input())
s = input().lower()
for i in s:
    a = ord(i) - n
    if a < 97:
        a = a + 26
    elif a >= 97:
        a = a

    print(chr(a), end='')