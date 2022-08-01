# python из верблюжьего регистра в змеиный регистр

def convert_to_python_case(text):
    res = [text[0].lower()]
    for c in text[1:]:
        if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
            res.append('_')
            res.append(c.lower())
        else:
            res.append(c)
     
    return ''.join(res)  

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))


@"222

import re
a = "ThisIsCamelCaseExample"
b=list(a)
[b.insert(x,'_') for x in [m.start() for m in re.finditer("[A-Z]",a)][:0:-1]]
res = ''.join(b).lower()
print(res)