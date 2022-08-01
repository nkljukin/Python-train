
n = int(input())
 
b = ''
 
while n > 0:
    b = str(n % 2) + b
    n = n // 2
 
print(b)


# put your python code here
n = int(input())

b = format(n, 'b')
print(b)