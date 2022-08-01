# проверка пароля

def is_password_good(password):
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    if len(password) >= 8:
        c4 += 1
    for i in password:
        if ord(i) in range(48, 58):
            c1 += 1
        if ord(i) in range(65, 91): # ABCDE
            c2 += 1
        if ord(i) in range(97, 123): # abcde
            c3 += 1
    
    print(c1, c2, c3, c4, len(password))

    if (c1 * c2 * c3 * c4) != 0:
        return print(True)
    else:
        return print(False)
    


# считываем данные
txt = input()

# вызываем функцию
is_password_good(txt)