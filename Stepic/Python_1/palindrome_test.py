# проверка на палиндром

def is_palindrome(text):

    s = list(text.lower())
    s1 = []
    for i in s:
        if i.isalpha():
            s1.append(i)
    
    if s1 == s1[::-1]:
        print(True)
    else:
        print(False)
 
# считываем данные
txt = input()

# вызываем функцию
is_palindrome(txt)