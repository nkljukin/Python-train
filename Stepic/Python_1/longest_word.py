# вывести самое длинное и короткое слово

a, b, c = str(input()), str(input()), str(input())

print(min(a, b, c, key=len))
print(max(a, b, c, key=len))